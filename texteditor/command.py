from __future__ import annotations
from abc import abstractmethod, ABC

class Command(ABC):
    @abstractmethod
    def do(self, text: str) -> str:
        pass

    @abstractmethod
    def undo(self, text:str) -> str:
        pass