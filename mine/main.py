from __future__ import annotations
from random import randint
from bacteria import Bacteria
from virus import Virus
from field import Field
from organism import Organism
from dl import DeathAndLife

# NUM_BACTERIAS = 3
# NUM_VIRUSES = 4

def print_field(field: Field):
    for i in range(field.rows):
        for j in range(field.cols):
            print(field.get_value(i, j), end='')
        print()
    print()

def pole_zhivi(dl: DeathAndLife):
    for organism in arr_organisms:
        organism.make_step()
        if organism.name == 'v ' and organism.steps == 5:
            dl.die_in_cell(organism.row, organism.col)

rows, cols = map(int, input('> Enter the size of your field: ').split())

# field = Field(rows, cols)

# organisms = []
# for i in range(NUM_BACTERIAS):
#     b = Bacteria(randint(0, rows - 1), randint(0, cols - 1), field)
#     field.set_value(b.row, b.col, b.name)
#     organisms.append(b)
# for i in range(NUM_VIRUSES):
#     v = Virus(randint(0, rows - 1), randint(0, cols - 1), field)
#     field.set_value(v.row, v.col, v.name)
#     organisms.append(v)

dl = DeathAndLife(rows, cols)

print_field(dl.field)
while True:
    pole_zhivi(dl)
    print_field(dl.field)
    x = input()
    if x != '':
        print(f'The simulation was cancelled with the key: {x}')
        break