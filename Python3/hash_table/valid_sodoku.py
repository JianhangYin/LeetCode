"""
Determine if a 9x9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

Each row must contain the digits 1-9 without repetition.
Each column must contain the digits 1-9 without repetition.
Each of the 9 3x3 sub-boxes of the grid must contain the digits 1-9 without repetition.

A partially filled sudoku which is valid.

The Sudoku board could be partially filled, where empty cells are filled with the character '.'.
"""

class Solution:
    def isValidSudoku(self, board: list) -> bool:
        for item in board:
            if not self.checkUnit(item):
                return False
        for item in zip(*board):
            if not self.checkUnit(item):
                return False
        for row in [0, 3, 6]:
            for col in [0, 3, 6]:
                item = []
                for i in range(3):
                    for j in range(3):
                        item.append(board[row + i][col + j])
                if not self.checkUnit(item):
                    return False
        return True

    def checkUnit(self, input_list):
        check_list = []
        for item in input_list:
            if item is not '.':
                check_list.append(item)
        return len(check_list) == len(set(check_list))

    def isValidSodukuFast(self, board: list) -> bool:
        hash_list = []
        for row in range(len(board)):
            for col in range(len(board)):
                num_val = board[row][col]
                if num_val is '.':
                    continue
                row_index = str(row) + '(' + str(num_val) + ')'
                col_index = '(' + str(num_val) + ')' + str(col)
                sec_index = str(row // 3) + '(' + str(num_val) + ')' + str(col // 3)
                if row_index in hash_list or col_index in hash_list or sec_index in hash_list:
                    return False
                else:
                    hash_list.append(row_index)
                    hash_list.append(col_index)
                    hash_list.append(sec_index)
        return True

