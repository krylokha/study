from __future__ import annotations
from typing import Callable, Any, Generator
import math

# Класс Time хранит значение часов, минут и секунд в пределах суток.
# Метод shift_seconds принимает количество секунд, на которое нужно сдвинуть текущее время
# и изменяет значения полей для того, чтобы выполнить этот сдвиг.

# Класс DateTime представляет собой дату (день, месяц, год) и время в этот день (часы, минуты, секунды). 
# DateTime наследуется от класса Time. 
# Метод shift_days() принимает количество дней и сдвигает дату на это количество дней.

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
        return f"Дата: {self.__day}.{self.__month:02}.{self.__year}, время: {self.h}:{self.m}:{self.s}"


day, month, year = map(int, input('Добро пожаловать в программу изменеия времени!\nВведите желаемую дату, которую хотите изменить в формате дд.мм.гггг >> ').split('.'))
hour, minute, second = map(int, input('Супер! А теперь введите время, которое желаете изменить в формате чч:мм:сс >> ').split(':'))
date = DateTime(hour, minute, second, day, month, year)
days = int(input('Введите то количество дней, на которое хотите перемотать время (можно с минусом) >> '))
date.shift_days(days)
sec = int(input('Введите то количество секунд, на которое хотите перемотать время (можно с минусом) >> '))
date.shift_seconds(sec)
print(f'Ваша дата получилась следующей: {date}')