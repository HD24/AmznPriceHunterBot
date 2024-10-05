# Amazon Price Hunter

Un bot de Telegram para monitorear precios de productos en Amazon. Agrega productos con un precio objetivo y recibirás una notificación cuando el precio baje.

## Características
- Agrega un producto para monitorear con `/add [URL] [precio objetivo]`.
- Notificaciones cuando el precio baja al valor deseado.
- Almacena productos en un archivo JSON.

## Requisitos
- Python 3.x
- Telegram Bot Token

## Instalación
1. Clona el repositorio.
2. Instala las dependencias:
    ```bash
    pip install -r requirements.txt
    ```
3. Coloca tu token de Telegram en un fichero `dev.env`.

## Uso
1. Ejecuta el bot:
    ```bash
    python telegram_bot.py
    ```
2. Usa los comandos en Telegram:
    - `/start` para iniciar.
    - `/add [URL] [precio]` para agregar un producto.
