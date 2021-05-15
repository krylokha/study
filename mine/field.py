from __future__ import annotations

class Field:
    rows: int
    cols: int

    def __init__(self, rows: int, cols: int):
        self.rows = rows
        self.cols = cols
        self.field = [['_ '] * cols for i in range(rows)]

    def get_value(self, row: int, col: int) -> str:
        return (self.field[row][col] if 0 <= row < self.rows and 0 <= col < self.cols else None)

    def generate_value(self, num: int, rows: int, cols: int, value: str):
        for i in range(num):
            row = random.randint(0, rows - 1)
            col = random.randint(0, cols - 1)
            self.set_value(row, col, value)

    def set_value(self, row: int, col: int, value: str):
            if self.is_empty(row, col):
                self.field[row][col] = value
 
    def is_empty(self, row: int, col: int) -> bool:
        if row < 0 or row >= self.rows or col < 0 or col >= self.cols:
            return False
        return self.field[row][col] == '_ '
    
    def delete_cell(self, row: int, col: int):
        if row < 0 or row >= self.rows or col < 0 or col >= self.cols:
            return False
        else:
            self.field[row][col] = '_ '