from __future__ import annotations
from abc import abstractmethod, ABC
from selection import Selection

class TagCommand(ABC):
    __open_tag: str
    __close_tag: str
    __sel: Selection


    def __init__(self, open_tag: str, close_tag: str, sel: Selection):
        self.__open_tag = open_tag
        self.__close_tag = close_tag
        self.__sel = sel


    def do(self, text: str) -> str:
        return (text[:self.__sel.start - 1] + self.__open_tag + 
                    text[self.__sel.start - 1:self.__sel.end] +
                    self.__close_tag + text[self.__sel.end:])


    def undo(self, text: str) -> str:
        tag_beginning = len(self.__open_tag)
        tag_ending = len(self.__close_tag)
        return (text[:self.__sel.start - 1] + 
                    text[self.__sel.start - 1 + tag_beginning:self.__sel.end - 1 + tag_ending] + 
                    text[self.__sel.end + 2 * tag_ending - 1:])