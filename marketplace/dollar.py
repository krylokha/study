from __future__ import annotations
from currency import Currency

class Dollar(Currency):
    DOLLAR: float = 75
    
    def get_course(self):
        return round(1 / self.DOLLAR)