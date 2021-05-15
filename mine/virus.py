from __future__ import annotations
from random import choice
from organism import Organism
from field import Field
from bacteria import Bacteria

LIMIT_STEPS = 5

class Virus(Organism):
    name: str = 'v '
    field: Field
    steps: int = 0

    def __init__(self, row: int, col: int, field: Field):
        super().__init__(row, col)
        self.field = field 

    def make_step(self):
        if self.eat():
            self.born()

    def eat(self) -> bool:
        cells_around = ((-1, 0), (-1, -1), (0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1))
        is_fed = False
        for cell in cells_around:
            if self.field.get_value(self.row + cell[0], self.col + cell[1]) == 'b ':
                self.field.set_value(self.row + cell[0], self.col + cell[1], '_ ')
                self.steps = 0
                is_fed = True
                break
        if not is_fed: 
            self.steps += 1
        if self.steps == LIMIT_STEPS:
            self.die()
        return is_fed

    def die(self):
        self.field.set_value(self.row, self.col, '_ ')

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
        

    
