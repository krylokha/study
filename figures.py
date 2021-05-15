# На плоскости могут быть заданы фигуры нескольких типов: Квадрат и Круг. 
# Пользователь задает с клавиатуры параметры фигуры 
# Для квадрата это размер стороны и координата левого верхнего угла.
# Для круга это радиус и координата цента.
# После этого пользователь вводит координаты точки. 
# Необходимо проверить, попала ли эта точка в фигуру.
# Проверку попадания вынести в отдельную функцию, которая может принимать фигуру любого типа.

from __future__ import annotations
from abc import ABC, abstractmethod

class Point:
    x: float
    y: float

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def find_distance(self, other: Point):
        return sqrt((self.x - other.x) ** 2 + (self.y - other.y) ** 2)


class Figure(ABC):
    @abstractmethod
    def get_figure_type(self) -> str:
        pass

    @abstractmethod
    def make_sth(self, other: Point) -> bool:
        pass

                
class Circle(Figure):
    radius: float
    p: Point

    def __init__(self, p: Point, radius: float):
        self.radius = radius
        self.p = p

    def get_figure_type(self) -> str:
        return 'You have chosen a circle.'

    def make_sth(self, other: Point) -> bool:
        return self.p.find_distance(other) <= self.radius
        

class Square(Figure):
    length: float
    p: Point

    def __init__(self, p: Point, length: float):
        self.length = length
        self.p = p

    def get_figure_type(self) -> str:
        return 'You have chosen a square.'
    
    def make_sth(self, other: Point):
        return other.x >= self.p.x and other.y >= self.p.y and other.x <= self.p.x + self.length and other.y <= self.p.y + self.length
        
        
def is_point_in_figure(figure: Figure, point: Point): 
    if figure.make_sth(point):
        print('Your point is inside the figure.')
    else:
        print('Your point is outside the figure.')

f = Square(Point(2, 2), 3)
point = Point(4, 4)
other_point = Point(6, 6)

is_point_in_figure(f, point)
is_point_in_figure(f, other_point)