from dataclasses import dataclass
from math import sqrt
from typing import Optional

@dataclass
class Point:
    x: float
    y: float

previous_point: Point = Point(0, 0)
length = 0
number = ['first', 'second', 'third', 'fourth', 'fifth', 'sixth', 'seventh', 'eighth', 'nineth', 'tenth']


def find_distance(distance, first_point: Point, second_point: Point) -> float:
    sum = (first_point.x - second_point.x) ** 2 + (first_point.y - second_point.y) ** 2
    distance += sqrt(sum)
    print(f'The length of your line is {distance}')
    return distance


n = int(input('Please enter the number of points: '))
for i in range(n):
    print(f'Enter the coordinates of the {number[i]} point: ')
    point = Point(*list(map(float, input("> ").split())))
    find_distance(length, point, previous_point)
    previous_point = point
