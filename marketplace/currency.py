# В маркетплейсе товары могут продаваться в рублях, долларах и евро.
# Пользователи могут покупать эти товары также в рублях, долларах и евро, 
# но при этом платить могут не в той валюте, которая заявлена в ценнике товара, 
# а той, которая им удобна (с конвертацией по курсу). 
# Реализовать такую систему классов маркетплейса, которая позволит решить подобную задачу.

from __future__ import annotations
from abc import ABC, abstractmethod

class Currency(ABC):
    value: float

    def __init__(self, value: float):
        self.value = value / self.get_course()
    
    def convert(self) -> float:
        return self.value * self.get_course()

    @abstractmethod
    def get_course(self):
        pass