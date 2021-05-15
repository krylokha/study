from __future__ import annotations
from undostack import UndoStack
from selection import Selection
from insertcommand import InsertCommand
from mbc import MakeBoldCommand
from mic import MakeItalicCommand
from muc import MakeUnderlineCommand

class Editor:
    __text: str
    __undo_stack: UndoStack


    def __init__(self, text: str = ''):
        self.__text = text
        self.__undo_stack = UndoStack()

    
    @property
    def text(self) -> str:
        return self.__text


    def select(self, frm: int, to: int) -> Selection:
        return Selection(frm, to)


    def find(self, what: str, after_pos: int = -1) -> Selection:
        index_from = self.__text.find(what, after_pos)
        index_to = index_from + len(what)
        return Selection(index_from, index_to)


    def insert(self, sel: Selection, what: str):
        cmd = InsertCommand(sel, what)
        self.__undo_stack.push(cmd)
        self.__text = cmd.do(self.__text)


    def make_bold(self, sel: Selection):
        cmd = MakeBoldCommand(sel)
        self.__undo_stack.push(cmd)
        self.__text = cmd.do(self.__text)


    def make_italic(self, sel: Selection):
        cmd = MakeItalicCommand(sel)
        self.__undo_stack.push(cmd)
        self.__text = cmd.do(self.__text)


    def make_underline(self, sel: Selection):
        cmd = MakeUnderlineCommand(sel)
        self.__undo_stack.push(cmd)
        self.__text = cmd.do(self.__text)


    def undo(self):
        cmd = self.__undo_stack.pop()
        if cmd is not None:
            self.__text = cmd.undo(self.__text)


def ask() -> int:
    print('\nWhat would you like to do? PRESS:\n' +
        '1 to enter some text.\n' +
        '2 to make a fragment bolder.\n' +
        '3 to make an italic fragment.\n' +
        '4 to underline fragment\n'+
        '5 to cancel last edit.\n' +
        '6 to quit.\n'
        )
    cmd = int(input('>> '))
    return cmd


def main():
    print('WELCOME TO THE WWTE!\nEnter tour text.')
    text = Editor(input('>> '))
    cmd = ask()

    while cmd != 6:
        if 1 <= cmd <= 4:
            start, end = map(int, input('Enter the indexes >>\n').split())
            sel = text.select(start, end)
        if cmd == 1:
            inserted_text = input('Enter your text >>\n')
            text.insert(sel, inserted_text)
        elif cmd == 2:
            text.make_bold(sel)
        elif cmd == 3:
            text.make_italic(sel)
        elif cmd == 4:
            text.make_underline(sel)
        elif cmd == 5:
            text.undo()
        print(f'Here\'s your text >>\n{text.text}')
        cmd = ask()

    print('You quitted the program.')

if __name__ == "__main__": 
    main()