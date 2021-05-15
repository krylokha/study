from __future__ import annotations
from currency import Currency

class Euro(Currency):
    EURO: float = 9
    
    def get_course(self):
        return round(1 / self.EURO)