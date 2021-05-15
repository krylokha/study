from __future__ import annotations
from typing import Callable, Any, Generator
import math

# Написать класс Time, который будет хранить значение часов, минут и секунд в пределах суток. 
# Написать конструктор, который принимает начальные значения полей класса и задает их собственно полям. 
# Поля сделать закрытыми (с двумя подчеркиваниями) и реализовать для них методы геттер и сеттер. 
# Написать метод shift_seconds, который принимает количество секунд, на которое нужно сдвинуть текущее время
# и изменяет значения полей для того, чтобы выполнить этот сдвиг.

# Написать класс DateTime, который представляет собой дату (день, месяц, год) и время в этот день (часы, минуты, секунды). 
# dayateTime должен наследовать от класса Time. 
# Предоставить новые поля -- день, месяц и год, создать для них геттеры и сеттеры (в виде свойств), а также позволить передавать их в конструкторе. 
# Реализовать метод shift_days(), который принимает количество дней и сдвигает дату на это количество дней. 
# Метод shift_seconds пока оставить без изменения

# Определить в классе Time функцию-хук, которая принимает количество суток, на которые происходит сдвиг в методе shift_seconds.
# Эта функция-хук должна быть пустой. Вызвать эту функцию в методе shift_seconds. 
# Переопределить функцию-хук в классе DateTime так, чтобы в ней происходил сдвиг на переданное количество дней.

class Time:
    __h: int
    __m: int
    __s: int

    def __init__(self, h: int, m: int, s: int):
        self.h = h
        self.m = m
        self.s = s

    def shift_seconds(self, seconds: int):
        minutes = (seconds + self.__s) // 60
        self.__s = (seconds + self.__s) % 60
        self.__h = (((minutes + self.__m) // 60) + self.__h) % 24
        self.__m = (minutes + self.__m) % 60
        days = seconds // 86400
        self._shift(days)
        
    
    def _shift(self, days: int):
        pass

    @property
    def h(self) -> int:
        return self.__h
    
    @property
    def m(self) -> int:
        return self.__m
    
    @property
    def s(self) -> int:
        return self.__s

    @h.setter
    def h(self,  h: int):
        if h not in (range(0, 24)):
            print('The hour must be between 0 anday 23!')
        else:
            self.__h = h
    
    @m.setter
    def m(self, m: int):
        if m not in (range(0, 60)):
            print('Minuts must be between 0 anday 59!')
        else:
            self.__m = m

    @s.setter
    def s(self, s: int):
        if s not in (range(0, 60)):
            print('Secondays must be between 0 anday 59!')
        else:    
            self.__s = s

    def __repr__(self) -> str:
        return f"{self.__h:02}:{self.__m:02}:{self.__s:02}"

class DateTime(Time):
    __day: int
    __month: int
    __year: int

    def __init__(self, h: int, m: int, s: int, day: int, month: int, year: int):
        super().__init__(h, m, s)
        self.year = year
        self.month = month
        self.day = day

    @property
    def day(self) -> int:
        return self.__day
        
    @property
    def month(self) -> int:
        return self.__month

    @property
    def year(self) -> int:
        return self.__year

    # Метод, проверяющий сколько дней в месяце days_check()
    # @staticmethod
    # def days_check(m: int):
    #     return months[m - 1]

    @day.setter
    def day(self, day: int):
        if DateTime.is_leap(self.__year) and self.__month == 2:
            if day < 1 or day > 29:
                print('Go away')
            else:
                self.__day = day
        elif self.__month == 2:
            if day < 1 or day > 28:
                print('Go away')
            else:
                self.__day = day
        elif self.__month in (4, 6, 9, 11):
            if day < 1 or day > 30:
                print('Go away')
            else:
                self.__day = day
        else:
            if day < 1 or day > 31:
                print('Go away')
            else:
                self.__day = day
            
                
    @month.setter
    def month(self, month: int):
        if month not in range(1, 13):
            print('Month is out of range!')
        else:
            self.__month = month
        
    @year.setter
    def year(self, year: int):
        if year == 0:
            print('Go away')
        else:
            self.__year = year

    def shift_days(self, days: int):
        months_leap = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

        savings = self.__day + days

        if DateTime.is_leap(self.__year):
            this_months = months_leap
        else:
            this_months = months

        while savings > this_months[self.__month - 1]:
            savings -= this_months[self.__month - 1]
            if self.__month != 12:
                self.__month += 1
            else:
                self.__month = 1
                self.__year += 1
                if DateTime.is_leap(self.__year):
                    this_months = months_leap
                else:
                    this_months = months

        while savings <= 0:
            savings += this_months[self.__month - 1]
            self.__month -= 1
            if self.__month <= 1 and savings <= 0:
                self.__month = 12
                self.__year -= 1
                if DateTime.is_leap(self.__year):
                    this_months = months_leap
                else:
                    this_months = months

        self.__day = savings

    def _shift(self, days: int):
        self.shift_days(days)


    @staticmethod
    def is_leap(year: int) -> bool:
        return year % 4 == 0 and year % 100 != 0 or year % 400 == 0

    def __repr__(self) -> str:
        return f"{self.__day}.{self.__month:02}.{self.__year}"


# time = Time(12, 59, 59)
date = DateTime(18, 45, 53, 30, 12, 2004)
# print(time)
print(date)
days = int(input())
date.shift_days(days)
sec = int(input())
date.shift_seconds(sec)
print(date)
# sec = int(input())
# time.shift_secondays(sec)
# print(time)