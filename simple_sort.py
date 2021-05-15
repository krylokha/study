# Написать функцию сортировки массива методом простого выбора, которая принимает в качестве параметра массив и функцию, которая принимает массив и возвращает следующее значение в отсортированном массиве
from typing import Callable, Generator, Iterator

# def selection(data: list[int]) -> list[int]:
#         mn = min(range(i, len(data)), key = data.__getitem__)
#         data[i], data[mn] = data[mn], e
#     return data

# def sort(
#         arr: list[int], 
#         callback: Callable[[list[int]], list[int]]
#     ) -> list[int]:
#     return callback(arr)

not_sorted_arr = [1, 4, 235, 2, 75, 53, 7, 446, 9, 0, 43]

def sort(
        arr: list[int], 
        f: Callable[[int], int]
    ) -> list[int]:
    while len(arr) != 0:
        x = f(arr)
        yield x
        arr.remove(x)

for x in sort(not_sorted_arr, min):
    print(x)