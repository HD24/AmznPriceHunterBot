import json
import os


class DataHandler:

    def __init__(self, filename='products.json'):
        self.filename = filename
        if not os.path.exists(self.filename):
            with open(self.filename, 'w') as file:
                json.dump([], file)

    def load_products(self):
        with open(self.filename, 'r') as file:
            return json.load(file)

    def save_products(self, products):
        with open(self.filename, 'w') as file:
            json.dump(products, file, indent=4)

    def add_product(self, url, target_price, chat_id):
        products = self.load_products()
        products.append({"url": url, "target_price": target_price, "chat_id": chat_id})
        self.save_products(products)

    def remove_product(self, url):
        products = self.load_products()
        products = [product for product in products if product['url'] != url]
        self.save_products(products)
