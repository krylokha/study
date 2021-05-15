from __future__ import annotations
from currency import Currency

class Product:
    name: str
    price: Currency

    def __init__(self, name: str, price: Currency):
        self.name = name
        self.price = price