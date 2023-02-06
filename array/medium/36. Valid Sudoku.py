# https://leetcode.com/problems/valid-sudoku/description/
# Determine if a 9 x 9 Sudoku board is valid.
# Only the filled cells need to be validated according to the following rules:
# Each row must contain the digits 1-9 without repetition.
# Each column must contain the digits 1-9 without repetition.
# Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition

# 用enumerate生成每筆資料的座標
# 用//(整除)得到每個sub box的座標
# 用座標區分不同row, col或box的資料
# 一個list可以不同行列的值，只用記錄第幾行列來區分
# TC: O(n^2)
# SC: O(n)
class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        temp_row = []
        temp_col = []
        temp_box = []
        
        for row, arr in enumerate(board):
            for col, val in enumerate(arr):
                
                if val != '.':
                    # check each row
                    if (col, val) not in temp_row:
                        temp_row.append((col, val))
                    else:
                        return False

                    # check each col
                    if (row, val) not in temp_col:
                        temp_col.append((row, val))
                    else:
                        return False

                    # check each block
                    if (col//3, row//3, val) not in temp_box:
                        temp_box.append((col//3, row//3, val))
                    else:
                        return False
        
        return True