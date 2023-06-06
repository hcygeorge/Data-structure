# 1st try: O(m*n)
class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        zero_row = []
        zero_col = []
        for row in range(len(matrix)):
            for col in range(len(matrix[row])):
                if matrix[row][col] == 0:
                    zero_row.append(row)
                    zero_col.append(col)
                    
        
        for row in range(len(matrix)):
            if row in zero_row:
                matrix[row] = [0] * len(matrix[row])
                continue
            for col in range(len(matrix[row])):
                if col in zero_col:
                    matrix[row][col] = 0
                    
                    
                    
                    