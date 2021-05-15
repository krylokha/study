# На прямоугольной поверхности живут бактерии и вирусы. 
# Бактерии каждую секунду с вероятностью 30% делятся на две.
# Вирусы каждую секунду пожирают находящуюся рядом бактерию. 
# Если они питались, значит с вероятностью 30%, они делятся на два. 
# Если в течение 5 секунд вирус не пожирал ни одну бактерию, он погибает. 
# Если рядом с вирусом находится несколько бактерий, он может выбрать любую. 
# Выполнить симуляцию этого процесса.

from __future__ import annotations
from abc import ABC, abstractmethod
import random

NUM_BACTERIAS = 3
NUM_VIRUSES = 4

class Field:
    rows: int
    cols: int

    def __init__(self, rows: int, cols: int):
        self._rows = rows
        self._cols = cols
        self._table = [['_ '] * cols for i in range(rows)]

    def get_value(self, row: int, col: int) -> bool:
        return (self._table[row][col] if 0 <= row < self._rows and 0 <= col < self._cols
                else None)
 
    def is_empty(self, row: int, col: int) -> bool:
        return self._table[row][col] == '_ '

    def set_value(self, num: int, rows: int, cols: int, value: str):
        for i in range(num):
            row = random.randint(0, rows - 1)
            col = random.randint(0, cols - 1)
            if self.is_empty(row, col):
                self._table[row][col] = value
 
    def n_rows(self) -> int:
        return self._rows
 
    def n_cols(self) -> int:
        return self._cols


class Organism(ABC):
    def count_percentage(self):
        percent = random.randint(0, 100)
        return percent >= 30

    @abstractmethod
    def step(self):
        pass

    @abstractmethod
    def is_alive(self):
        pass


class Bacteria(Organism):
    field: Field
    bacteria_places: list[int]

    def make_babies(self, field: Field):
        rows = []
        cols = []
        for i in range(field.rows):
            for j in range(field.cols):
                if field.get_value(i, j) == 'b ':
                    if i != 0 or i != field.rows - 1 or j != 0 or j != field.cols - 1 :
                    rows.append(i)
                    rows.append(i - 1)
                    rows.append(i + 1)

                    cols.append(j)
                    cols.append(j - 1)
                    cols.append(j + 1)
                    for k in range(2):
                        row = random.choice(rows)
                        col = randpm.choice(cols)
                    if field.is_empty(row, col) and self.count_percentage():
                        field.set_value(row, col) = 'b '

    def step(self):
        pass

    def is_alive(self):
        pass


class Virus(Organism):
    field: Field
    viruses_places: list[int] = []

    def is_fed_up(self, field: Field):

    def make_babies(self, field: Field, i: int, j: int):
        pass

    def step(self):
        pass

    def is_alive(self):
        pass
    

cols, rows = map(int, input('> Enter the size of your field: ').split())

field = Field(rows, cols)

# virus = Virus()
bacteria = Bacteria()

field.set_value(NUM_BACTERIAS, rows, cols, 'b ')
field.set_value(NUM_VIRUSES, rows, cols, 'v ')

for i in range(field.n_rows()):
    for j in range(field.n_cols()):
        print(field.get_value(i, j), end='')
    print()
print()


bacteria.make_babies(field)