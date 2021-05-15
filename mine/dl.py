from __future__ import annotations
from organism import Organism
from virus import Virus
from bacteria import Bacteria
from field import Field
import constant

class DeathAndLife:
    organisms: list[Organism]
    field: Field

    def __init__(self, rows: int, cols: int):
        self.field = Field(rows, cols)
        self.organisms = []
        for i in range(constant.NUM_BACTERIAS):
            b = Bacteria(randint(0, rows - 1), randint(0, cols - 1), field)
            self.field.set_value(b.row, b.col, b.name)
            self.organisms.append(b)
        for i in range(constant.NUM_VIRUSES):
            v = Virus(randint(0, rows - 1), randint(0, cols - 1), field)
            self.field.set_value(v.row, v.col, v.name)
            self.organisms.append(v)

    def die(self, org: Organism):
        self.field.delete_in_cell(org.row, org.col)
        self.organisms.remove(org)

    def die_in_cell(self, row: int, col: int):
        for organism in self.organisms:
            if organism.row == row and organism.col == col:
                self.die(organism)
                return

