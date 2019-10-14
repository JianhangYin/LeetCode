"""
You are given an n x n 2D matrix representing an image.

Rotate the image by 90 degrees (clockwise).

Note:

You have to rotate the image in-place, which means you have to modify the input 2D matrix directly.
DO NOT allocate another 2D matrix and do the rotation.
"""


class Solution:
    def rotate(self, matrix: list) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        length = len(matrix)
        for row in range(length // 2):
            for col in range(row, length - row - 1):
                first = True
                row_pointer = row
                col_pointer = col
                cur = matrix[row_pointer][col_pointer]
                while not (row_pointer == row and col_pointer == col) or first:
                    first = False
                    row_pointer, col_pointer = col_pointer, length - row_pointer - 1
                    temp = matrix[row_pointer][col_pointer]
                    matrix[row_pointer][col_pointer] = cur
                    cur = temp
        return




