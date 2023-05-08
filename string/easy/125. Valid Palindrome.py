# A phrase is a palindrome if, after converting all uppercase letters into lowercase letters 
# and removing all non-alphanumeric characters, it reads the same forward and backward. 
# Alphanumeric characters include letters and numbers.
# Given a string s, return true if it is a palindrome, or false otherwise.

# tips:
# 用左右指針檢查兩側字母是否相同
# 字串中的非字母數字可以先移除，或是比較時直接跳過就好

# first try
class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """

        p1, p2 = 0, len(s) - 1

        while p1 < p2:
            if not s[p1].isalnum():
                p1 += 1
                continue

            if not s[p2].isalnum():
                p2 -= 1
                continue

            if s[p1].lower() != s[p2].lower():
                return False
            else:
                p1 += 1
                p2 -= 1

        return True