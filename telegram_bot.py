import os

from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes, JobQueue
from price_tracker import SmartPriceTracker
from data_handler import DataHandler
from dotenv import load_dotenv

load_dotenv('dev.env')

TOKEN = os.getenv("TELEGRAM_TOKEN")
data_handler = DataHandler()


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('¡Bienvenido! Usa /add [URL] [precio] para monitorear un producto.')


async def add_product(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        url = context.args[0]
        target_price = float(context.args[1])
        chat_id = update.message.chat_id

        data_handler.add_product(url, target_price, chat_id)
        await update.message.reply_text(f'Producto agregado: {url} con precio objetivo: {target_price}')
    except IndexError:
        await update.message.reply_text('Por favor, usa el formato: /add [URL] [precio]')
    except ValueError:
        await update.message.reply_text('El precio debe ser un número.')


async def check_prices(context: ContextTypes.DEFAULT_TYPE):
    print("Checking prices...")
    products = data_handler.load_products()
    smart_tracker = SmartPriceTracker()
    for product in products:
        url = product['url']
        target_price = product['target_price']
        chat_id = product['chat_id']
        current_price = smart_tracker.get_price(url)

        if current_price is not None and current_price <= target_price:
            await context.bot.send_message(chat_id, f'¡El precio ha bajado! {url} ahora cuesta {current_price}')
            data_handler.remove_product(url)


def main():
    application = Application.builder().token(TOKEN).build()

    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("add", add_product))

    job_queue = application.job_queue
    job_queue.run_repeating(check_prices, interval=3600, first=10)

    application.run_polling()


if __name__ == '__main__':
    main()

