from __future__ import annotations
from selection import Selection
from command import Command

class InsertCommand(Command):
    __sel: Selection
    __erased_text: str
    __inserted_text: str

    def __init__(self, sel: Selection, inserted_text: str = ''):
        self.__sel = sel
        self.__inserted_text = inserted_text
        self.__erased_text = ''
    
    def do(self, text: str) -> str:
        self.__erased_text = text[self.__sel.start - 1:self.__sel.end]
        return text[:self.__sel.start - 1] + self.__inserted_text + text[self.__sel.end:]

    def undo(self, text: str) -> str:
        inserted = len(self.__inserted_text)
        return text[:self.__sel.start - 1] + self.__erased_text + text[self.__sel.start - 1 + inserted:]