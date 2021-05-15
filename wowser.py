import os


def wow(directory):
    for path in os.listdir(directory):
        path = os.path.join(directory, path)
        if os.path.isfile(path):
            yield path
        elif os.path.isdir(path):
            yield from wow(path)


folder = os.path.abspath(input())

for x in wow(folder):
    print(x)