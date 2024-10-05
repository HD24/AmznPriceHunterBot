import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
import time
import random


class SmartPriceTracker:
    def __init__(self):
        self.session = requests.Session()
        self.headers = {'User-Agent': UserAgent().random}
        custom_headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36"
        }
        self.headers = custom_headers

    def get_price(self, url):
        try:
            # Añadir un retardo aleatorio para parecer más humano
            time.sleep(random.uniform(2, 5))

            # Hacer la solicitud
            response = self.session.get(url, headers=self.headers)
            soup = BeautifulSoup(response.content, 'html.parser')

            # Extraer el precio (usa selectores CSS robustos)
            price_element = soup.find(class_="a-price aok-align-center reinventPricePriceToPayMargin priceToPay")
            if price_element:
                # Eliminar caracteres innecesarios y convertir a número
                price = price_element.get_text().replace('€', '').replace('.', '').replace(',','.').strip()
                return float(price)
            else:
                print("No se encontró el precio en la página.")
                return None
        except Exception as e:
            print(f"Error al obtener el precio: {e}")
            return None



