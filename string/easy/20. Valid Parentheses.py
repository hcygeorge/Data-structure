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
        dic = {
            '(': ')',
            '[': ']',
            '{': '}'
            }
        stack = []
        
        for char in s:
            if dic.get(char):
                stack.append(char)
            else:
                if not stack:
                    return False
                if char == dic.get(stack.pop()):
                    continue
                return False
        
        return len(stack) == 0

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