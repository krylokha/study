# Объявляем dataclass Student. Ученик: ФИО, группа и список оценок. Пустой массив оценок -- не отличник и не двоечник.
# Ввести n -- кол-во учеников, после чего ввести информацию о них и запомнить в массив. Определить учеников-отличников и вывести их ФИО. Определить учеников-неуспевающих и вывести их ФИО. Вывести в столбик.
# отличники -- ученики, у которых все оценки == 5
# неуспевающие -- ученики, у которых есть хотя бы одна оценка < 3.

from dataclasses import dataclass

@dataclass
class Student:
    name: str
    group: str
    marks: list[int]

fives = 0
twos = 0
best_students = []
worst_students = []


def best_student(marks: list[int]) -> bool:
    for i in range (len(marks)):
        if marks[i] != 5:
            return False
    return True


def worst_student(marks: list[int]) -> bool:
    for i in range(len(marks)):
        if marks[i] < 3:
            return True
    return False
    

n = int(input('Enter the amount of students please: '))
students: list[Student] = []

for i in range(n):
    student_name = input('Enter student\'s name: ')
    student_group = input('Enter student\'s group: ')
    student_marks = list(map(int, input('Enter students marks: ').split()))
    if best_student(student_marks):
        fives += 1
        best_students.append(student_name)
    if worst_student(student_marks):
        twos +=1
        worst_students.append(student_name)
    student: Student = Student(name=student_name, group=student_group, marks=student_marks)
    students.append(student)

print(f'The amount of the best students is {fives}, their names are {", ".join(best_students)}.')
print(f'The amount of the worst students is {twos}, their names are {", ".join(worst_students)}')