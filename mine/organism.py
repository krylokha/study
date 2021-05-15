from __future__ import annotations
from abc import ABC, abstractmethod
from random import uniform
import dl

class Organism(ABC):
    row: int
    col: int
    percent: float

    def __init__(self, row: int, col: int):
        self.row = row
        self.col = col

    def do(self) -> bool:
        self.percent = uniform(0, 100)
        return self.percent >= 30.0

    @abstractmethod
    def make_step(self):
        pass