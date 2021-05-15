from typing import Callable, Generator
# Написать функцию, которая принимает требуемое количество чисел Фибоначчи и возвращает генератор (yield) этих чисел

sequence = [1, 1]
x, y = 1, 1

def fibonacci(member, arr: list[int]) -> list:
    for i in range(2, member):
        arr.append(arr[i- 1] + arr[i - 2])
    yield arr

n = int(input('Please enter the number of fibonacci sequence members: '))

for x in fibonacci(n, sequence):
    print(x)