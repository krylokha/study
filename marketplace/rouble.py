from __future__ import annotations
from currency import Currency

class Rouble(Currency):
    RUB: float = 1
    
    def get_course(self):
        return round(1 / self.RUB)
