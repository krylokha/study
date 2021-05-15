# Мальчики и девочки сдают зачет по физкультуре. 
# Мальчики должны сделать 20 отжиманий на зачет. 
# Девочки должны сделать 20 приседаний на зачет. 
# Класс состоит и мальчиков и девочек вперемешку. 
# Написать программу, которая проводит зачет в этом классе.

from abc import ABC, abstractmethod
from typing import Callable, Generator, Iterator
import random


class Student(ABC):
    name: str
    quantity: int

    def __init__(self, name):
        self.name = name
        self.quantity = random.randint(1, 40)

    @abstractmethod
    def get_result(self) -> bool:
        pass


class Female(Student):
    def __init__(self, name: str):
        super().__init__(name)

    def get_result(self) -> bool:
        return self.quantity >= 20


class Male(Student):
    def __init__(self, name: str):
        super().__init__(name)

    def get_result(self) -> bool:
        return self.quantity >= 20


def try_pass(student: Student):
    if student.get_result():
        print(f'Student {student.name} passed the exam with the result {student.quantity}')
    else:
        print(f'Student {student.name} did not pass the exam with the result {student.quantity}')


Students_list = [   Female('Maria'), 
                    Male('Alex'), 
                    Female('Alena'), 
                    Male('Ivan'), 
                    Male('Igor'), 
                    Male('Ilia'), 
                    Female('Lisa'), 
                    Male('Timer'), 
                    Female('Irina'), 
                    Female('Sofia'), 
                    Male('Andrey'), 
                    Female('Valentina'), 
                    Male('Dmitry')
                    ]

for student in Students_list:
    try_pass(student)
