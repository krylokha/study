from __future__ import annotations

class Selection:
    start: int
    end: int

    def __init__(self, start: int, end: int):
        self.start = start
        self.end = end
