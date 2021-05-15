import os

folder = os.path.abspath(input())

def wow(directory):
    for path in os.listdir(directory):
        path = os.path.join(directory)
        if os.path.isfile(path):
            yield path
        elif os.path.isdir(path):
            yield from wow(path)

for x in wow(folder):
    print(x)