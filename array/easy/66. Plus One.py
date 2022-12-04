# You are given a large integer represented as an integer array digits, 
# where each digits[i] is the ith digit of the integer. 
# The digits are ordered from most significant to least significant in left-to-right order. 
# The large integer does not contain any leading 0's.

# 從arr尾端檢查每個位數，如果加1後小於10，則回傳答案，若為10，則要歸0並檢查下個位數
# 如果arr內全為9則要在最左邊插入1
class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        
        for idx in range(len(digits)-1, -1, -1):
            if digits[idx] + 1 < 10:
                digits[idx] += 1
                return digits
            else:
                digits[idx] = 0
                
        return [1] + digits