# tips: 遇到左括號先存在stack，遇到右括號時取最後一個左括號比對


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
