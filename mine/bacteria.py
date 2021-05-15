from __future__ import annotations
from random import choice
from organism import Organism
from field import Field


class Bacteria(Organism):
    name: str = 'b '
    field: Field

    def __init__(self, row: int, col: int, field: Field):
        super().__init__(row, col)
        self.field = field

    def make_step(self):
        self.born()
    
    def born(self):
        cells_around = ((-1, 0), (-1, -1), (0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1))
        random_sequence= []
        for cell in cells_around:
            if self.field.is_empty(self.row + cell[0], self.col + cell[1]):
                random_sequence.append((self.row + cell[0], self.col + cell[1]))
        if len(random_sequence) > 0:
            if self.do():
                for i in range(2):
                    cell = choice(random_sequence)
                    row, col = cell
                    self.field.set_value(row, col, self.name)
            




    
