# You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).
# You have to rotate the image in-place, 
# which means you have to modify the input 2D matrix directly. DO NOT allocate another 2D matrix and do the rotation.

# tips:
# 走訪矩陣左上半部的元素，然後順時鐘交換四個角的元素位置
# 或轉置+水平翻轉，水平翻轉+轉置會變成矩陣逆時鐘轉90度
# 或垂直翻轉+轉置


# blind spot:
# 走訪矩陣左上半部的元素需要考慮奇數情況，用n%2
# 轉置需要只走嚴格上三角矩陣，for j in range(i+1, n)

# first try: 交換四個角的位置
class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix[0])
        
        # 走訪矩陣位於左上角的元素
        for i in range(n//2 + n % 2):  # + n % 2是為了在長度為奇數的矩陣，走訪行或列在中間的元素
            for j in range(n//2):
                # 四個角順時鐘交換位置
                temp = matrix[i][j]  # 存左上角
                matrix[i][j] = matrix[n-1-j][i]  # 左下覆蓋左上
                matrix[n-1-j][i] = matrix[n-1-i][n-1-j]  # 右下覆蓋左下
                matrix[n-1-i][n-1-j] = matrix[j][n-1-i]  # 右上覆蓋右下
                matrix[j][n-1-i] = temp  # 左上覆蓋右上

# first try: 轉置+水平翻轉
class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        # self.transpose(matrix)
        # self.horizontal_reflect(matrix)

        self.vertical_reflect(matrix)
        self.transpose(matrix)
    
    def transpose(self, matrix):
        n = len(matrix)
        # range(i+1, n)只走訪嚴格上三角矩陣(不含對角線)的元素
        for i in range(n):
            for j in range(i+1, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    
    def horizontal_reflect(self, matrix):
        n = len(matrix)
        # range(n // 2)只走訪左半邊的元素
        for i in range(n):
            for j in range(n // 2):
                matrix[i][j], matrix[i][n-1-j] = matrix[i][n-1-j], matrix[i][j]

    def vertical_reflect(self, matrix):
        n = len(matrix)
        for i in range(n // 2):
            for j in range(n):
                matrix[i][j], matrix[n-1-i][j] = matrix[n-1-i][j], matrix[i][j]
            