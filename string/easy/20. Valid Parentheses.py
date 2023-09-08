
# tips:
# 每個右括弧一定要和"最後一個"左括弧配對到，
# 可利用stack儲存左括弧，再遇到右括弧時pop出左括弧比對
# 注意只有一個括弧以及全部都是右括弧的狀況

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


# 3rd try
class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        bracket = {'(': ')', '{': '}', '[': ']'}
        stack = []

        for i in s:
            if bracket.get(i):
                stack.append(i)
            else:
                if len(stack) == 0 or bracket.get(stack.pop()) != i:
                    return False
        
        return len(stack) == 0
