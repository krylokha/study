from __future__ import annotations
from command import Command

class UndoStack:
    __commands: list[Command]

    def __init__(self):
        self.__commands = []

    def push(self, cmd: Command):
        self.__commands.append(cmd)

    def pop(self) -> Command:
        if len(self.__commands) != 0:
            return self.__commands.pop()
        return None