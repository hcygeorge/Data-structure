
# tips:
# 先遇到的右括號一定要和最後一個左括號配對到
# 使用stack儲存左括號
# attempt count: 2

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """

        stack = []
        pare = {'{': '}', '[': ']', '(': ')'}

        p = 0
        while p < len(s):
            if pare.get(s[p]):
                stack.append(s[p])
                p += 1
                continue
            
            if stack:
                left = stack.pop()
            else:
                return False
                
            if s[p] == pare.get(left):
                p += 1
                continue
            else:
                return False

        return not stack


# 2nd try: same as before
class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        pare = {'{': '}', '(': ')', '[': ']'}
        left = []

        for char in s:
            if pare.get(char):
                left.append(char)
            else:
                if len(left) == 0:
                    return False

                if pare.get(left.pop()) != char:
                    return False
        
        return len(left) == 0
