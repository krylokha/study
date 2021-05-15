from __future__ import annotations
from typing import Callable, Any

class Time:
    __h: int
    __m: int
    __s: int

    def __init__(self, h: int, m: int, s: int):
        self.h = h
        self.m = m
        self.s = s

    def shift_seconds(self, seconds: int):
        # if self.__s // 60 == 1:
        #     self.__m += 1
        #     if self.__m // 60 == 1:
        #         self.__h += 1
        #         self.__m = 0
        #     self.__s = 0
        minutes = (seconds + self.__s) // 60
        self.__s = (seconds + self.__s) % 60
        self.__h = (((minutes + self.__m) // 60) + self.__h) % 24
        self.__m = (minutes + self.__m) % 60
        
    
    # def can_continue(variable: int):
    #     if variable not in list(range(0, 59)):
    #         print('The time unit must be between 0 and 59! ')
    #         return True
    #     return False

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
            print('The hour must be between 0 and 23!')
        else:
            self.__h = h
    
    @m.setter
    def m(self, m: int):
        if m not in (range(0, 60)):
            print('Minuts must be between 0 and 59!')
        else:
            self.__m = m

    @s.setter
    def s(self, s: int):
        if s not in (range(0, 60)):
            print('Seconds must be between 0 and 59!')
        else:    
            self.__s = s

    def __repr__(self) -> str:
        return f"{self.__h:02}:{self.__m:02}:{self.__s:02}"


time = Time(12, 59, 59)
print(time)
sec = int(input())
time.shift_seconds(sec)
print(time)