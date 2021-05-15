import os

up = os.path.dirname
start = up(up(up(up(up(os.path.abspath(__file__))))))
# print(start)
new_path = []

test_path = os.path.join(start, new_path)
print(test_path)
# def print_dir():
#     t