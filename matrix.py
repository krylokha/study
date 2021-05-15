from __future__ import annotations
from random import randint
from typing import Callable

class Matrix:
    rows: int
    cols: int    
    
    def __init__(self, rows: int, cols: int):
        self.rows = rows
        self.cols = cols
        self.matrix = []

    def print_matrix(self) -> str:
        matrix_rows = []
        for i in range(self.rows):
            for j in range(self.cols):
                x = randint(1, 50)
                matrix_rows.append(x)
            self.matrix.append(matrix_rows)
            matrix_rows = []
        print(self.matrix)

    def size_is_fine(self, other: Matrix) -> bool:
        return self.rows == other.rows and self.cols == other.cols

    def __add__(self, other: Matrix):
        third_rows = []
        third = []
        if self.size_is_fine(other):
            for i in range(self.rows):
                for j in range(self.cols):
                    third_rows.append(self.matrix[i][j] + other.matrix[i][j])
                third.append(third_rows)
                third_rows = []
            mtrx = Matrix(self.rows, self.cols)
            mtrx = third
            return mtrx
        raise ValueError('We cannot add the first matrix with the second matrix in spite of their sizes are different.')

    def __sub__(self, other: Matrix):
        third_rows = []
        third = []
        if self.size_is_fine(other):
            for i in range(self.rows):
                for j in range(self.cols):
                    third_rows.append(self.matrix[i][j] - other.matrix[i][j])
                third.append(third_rows)
                third_rows = []
            return third
        raise ValueError('We cannot subtrack the first matrix with the second matrix in spite of their sizes are different.')

    def __mul__(self, other: Matrix):
        if isinstance(other, Matrix):
            if self.cols != other.rows:
                raise ValueError('We cannot multiply the first matrix with the second matrix in spite of their sizes are unmatching.')
            third_rows = []
            third = []
            for i in range(self.rows):
                for j in range(other.cols):
                    summ = 0
                    for k in range(self.cols):
                        summ += self.matrix[i][k] * other.matrix[k][j]
                    third_rows.append(summ)
                third.append(third_rows)
                third_rows = []
                
            mtrx = Matrix(self.rows, self.cols)
            mtrx = third
            return mtrx
            # return third
        third_rows = []
        third = []
        for i in range(self.rows):
            for j in range(self.cols):
                third_rows.append(other * self.matrix[i][j])
            third.append(third_rows)
            third_rows =[]
        return third


# create Matrix 1
rows = int(input('Enter the number of rows:\n>> '))
cols = int(input('Enter the number of columns:\n>> '))
m1 = Matrix(rows, cols)
m1.print_matrix()

# Create Matrix 2
rows1 = int(input('Enter the number of rows in the other matrix:\n>> '))
cols1 = int(input('Enter the number of columns in the other matrix:\n>> '))
m2 = Matrix(rows1, cols1)
m2.print_matrix()

num = int(input)

# # We added 1st to the 2nd
# result_add = m1 + m2
# print('The sum of your matrices is THIS >>')
# print(result_add)

# # We subtracked 2nd from 1st
# result_sub = m1 - m2
# print('The difference between your matrices is THIS >>')
# print(result_sub)

# We multiplied 1st and 2nd
result_mul = m1 * m2
print('The product of matrices is THIS >>')
print(result_mul)