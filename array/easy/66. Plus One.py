# You are given a large integer represented as an integer array digits, 
# where each digits[i] is the ith digit of the integer. 
# The digits are ordered from most significant to least significant in left-to-right order. 
# The large integer does not contain any leading 0's.

# 從array尾端檢查每個位數，如果等於9則改為0(進位)然後檢查下一位數，否則加1後回傳答案
# 如果能走訪完整個array(內全為9)，則要在最左邊插入1(進位)
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
                
        return [1] + digits  # 完整迭代完表示需要插入新位數

# second try
class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        l = len(digits)

        for i in range(l-1, -1, -1):
            if digits[i] == 9:
                digits[i] = 0
            else:
                digits[i] += 1
                return digits

        digits.insert(0, 1)
        return digits
        