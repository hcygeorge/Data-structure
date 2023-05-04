# Implement the myAtoi(string s) function, which converts a string to a 32-bit signed integer (similar to C/C++'s atoi function).

# The algorithm for myAtoi(string s) is as follows:

# Read in and ignore any leading whitespace.
# Check if the next character (if not already at the end of the string) is '-' or '+'. Read this character in if it is either. This determines if the final result is negative or positive respectively. Assume the result is positive if neither is present.
# Read in next the characters until the next non-digit character or the end of the input is reached. The rest of the string is ignored.
# Convert these digits into an integer (i.e. "123" -> 123, "0032" -> 32). If no digits were read, then the integer is 0. Change the sign as necessary (from step 2).
# If the integer is out of the 32-bit signed integer range [-231, 231 - 1], then clamp the integer so that it remains in the range. Specifically, integers less than -231 should be clamped to -231, and integers greater than 231 - 1 should be clamped to 231 - 1.
# Return the integer as the final result.


# tips:
# 用指針走訪比for loop好，因為可以隨時跳出迴圈檢查條件，再從指針停留的地方繼續走
# 這題的例外很多，建議明確將空格、正負號或數字分開檢查，符合條件再繼續，不建議一次檢查所有狀況

# first try: 
class Solution(object):
    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """
        digits = ''
        sign = 1
        
        if s.strip() == '':
            return 0
        
        if len(s) == 1 and not s.isnumeric():
            return 0
        
        for idx, char in enumerate(s):
            if char == ' ':
                continue
            elif char.isalpha():
                return 0
            elif char == '-':
                if not s[idx + 1].isnumeric():
                    return 0
                sign = -1
                idx += 1
                break
            elif char == '+':
                if not s[idx + 1].isnumeric():
                    return 0
                sign = 1
                idx += 1
                break
            elif char.isnumeric():
                break
            else:
                return 0
            
        for i in range(idx, len(s)):
            print(s[i])
            if s[i].isnumeric():
                digits += s[i]
            else:
                break
                
        result = sign * int(digits)
        
        if result > 2**31-1:
            return 2**31-1
        elif result < -2**(31):
            return -2**31
        else:
            return result
        
class Solution(object):
    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """
        digits = ''
        sign = 1
        p = 0
        
        # whitespace only case
        if s.strip() == '':
            return 0
        
        # 1 char case
        if len(s) == 1 and not s.isnumeric():
            return 0
        
        # check and iterate through the whitespaces
        while p < len(s):
            if s[p] == ' ':
                p += 1
            else:
                break
        
        # extract sign from the string and make sure there is only one sign
        if s[p] == '+' and s[p+1].isnumeric():
            p += 1
        elif s[p] == '-' and s[p+1].isnumeric():
            sign = -1
            p += 1
        elif s[p].isnumeric():
            pass
        else:
            return 0
        
        # collect digits after sign
        while p < len(s):
            if s[p].isnumeric():
                digits += s[p]
                p += 1
            else:
                break
            
        result = sign * int(digits)
        
        # clamp in 32bit integer
        if result > 2**31-1:
            return 2**31-1
        elif result < -2**(31):
            return -2**31
        else:
            return result