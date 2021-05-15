# Мальчики и девочки сдают зачет по физкультуре. 
# Мальчики должны сделать 20 отжиманий на зачет. 
# Девочки должны сделать 20 приседаний на зачет. 
# Класс состоит и мальчиков и девочек вперемешку. 
# Количество отжиманий, приседаний генерируются автоматически.
# Программа определяет, кто сдал экзамен, а кто нет.

from abc import ABC, abstractmethod
from typing import Callable, Generator, Iterator
import random
import time

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
        print(f'Ученик(ца) {student.name} сдал(а) зачёт с результатом {student.quantity}.')
    else:
        print(f'Ученик(ца) {student.name} не сдал(а) зачёт с результатом {student.quantity}.')


Students_list = [   Female('Мария'), 
                    Male('Алексей'), 
                    Female('Алёна'), 
                    Male('Иван'), 
                    Male('Игорь'), 
                    Male('Илья'), 
                    Female('Елизавета'), 
                    Male('Тимер'), 
                    Female('Ирина'), 
                    Female('София'), 
                    Male('Андрей'), 
                    Female('Валентина'), 
                    Male('Дмитрий')
                    ]

print('Эта программа проводит зачёт у студентов в классе.\nИмена учеников известны. Количество упражнений генерируются автоматически.\nЧтоб сдать зачёт, девочкам требуется сделать 20 приседаний, мальчикам - 20 отжиманий.\nНажмите 1, когда будете готовы.')
x = int(input())
if x == 1:
        for student in Students_list:
            time.sleep(2)
            try_pass(student)
