# В маркетплейсе товары могут продаваться в рублях, долларах и евро.
# Пользователи могут покупать эти товары также в рублях, долларах и евро, 
# но при этом платить могут не в той валюте, которая заявлена в ценнике товара, 
# а той, которая им удобна (с конвертацией по курсу). 
# Реализовать такую систему классов маркетплейса, которая позволит решить подобную задачу.

from __future__ import annotations
from product import Product
from currency import Currency
from rouble import Rouble
from dollar import Dollar
from euro import Euro

class Marketplace:
    def __init__(self):
        self.products = {
            "Мясо": [Product("Мясо", Rouble(200)), Product("Мясо", Rouble(200)), Product("Мясо", Rouble(200))],
            "Рыба": [Product("Рыба", Dollar(15))],
            "Молоко": [Product("Молоко", Euro(0.9))],
            "Хлеб": [Product("Хлеб", Rouble(35)), Product("Хлеб", Rouble(35)), Product("Хлеб", Rouble(35)), Product("Хлеб", Rouble(35)), Product("Хлеб", Rouble(35))],
            "Пирожки с вишней": [Product("Пирожки с вишней", Dollar(1)), Product("Пирожки с вишней", Dollar(1)), Product("Пирожки с вишней", Dollar(1))],
            "Торт": [Product("Торт", Euro(5))],
            "Масло": [Product("Масло", Rouble(60)), Product("Масло", Rouble(60))],
            "Колбаса": [Product("Колбаса", Dollar(3))],
            "Тунец": [Product("Тунец", Rouble(125)), Product("Тунец", Rouble(125)), Product("Тунец", Rouble(125)), Product("Тунец", Rouble(125)), Product("Тунец", Rouble(125))],
            "Оливки": [Product("Оливки", Euro(2.5)), Product("Оливки", Euro(2.5)), Product("Оливки", Euro(2.5))],
        }

    def print_products(self) -> str:
        print("Какой товар вы желаете приобрести? Мы можем вам предложить: ")
        for product in self.products:
            print(product)

    # функция, которая "продаёт" наш товар и удаляет единицу товара из списка
    def sell(self, product: str):
        product = str(input("Теперь введите наименование товара, который вы хотите купить >> "))
        curr = str(input("Введите валюту, которой вы хотите оплатить товар (RUB, USD, EUR) >> "))
        summ = float(input("Введите сумму, которой вы располагаете >> "))

        if curr == "RUB":
            user_sum = Rouble(summ)
        elif curr == "USD":
            user_sum = Dollar(summ)
        else:
            user_sum = Euro(summ)

        for i in range(len(self.products)):
            if self.products[i] == product:
                if self.check(user_sum, product):
                    the_product = self.products.pop()
                    user_summ.value -= the_product.price.value

    # функция, которая проверяет, хватает ли пользователю денег
    def check(self, s: Currency, product_name: str) -> bool:
        product_needed = self.products[product_name][0]
        return s.value >= product_needed.price.value


Marketplace.print_products()
Marketplace.sell()