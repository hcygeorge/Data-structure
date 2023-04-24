# Given a signed 32-bit integer x, return x with its digits reversed. 
# If reversing x causes the value to go outside the signed 32-bit integer range [-2**31, 2**31 - 1], then return 0.
# Assume the environment does not allow you to store 64-bit integers (signed or unsigned).

# 用python的slice反轉操作
class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if abs(x) == x:
            output = int(str(x)[::-1])
        else:
            output = -int(str(abs(x))[::-1])
            
        if abs(output) > 2**31 -1:
            return 0
        
        return output
    
# 利用除法取出整數的尾數
# 負整數的餘數與正整數不同，因此統一先換成正整數再做除法
# O(log_x^n), O(1)，因為整數x會有log_10(x) + 1個位數
class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        rev = 0
        if abs(x) == x:
            sign = 1
        else:
            sign = -1

        x = abs(x)
        while x != 0:
            pop = x % 10
            x /= 10
            if (rev > (2**31- 1)/10) | ((rev == (2**31- 1)/10) & pop > 7):  # 因為2**31-1尾數是7，所以加7後溢位
                return 0
            else:
                rev = rev * 10 + pop

        return rev * sign