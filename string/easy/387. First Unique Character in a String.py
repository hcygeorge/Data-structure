# Given a string s, find the first non-repeating character in it and return its index.
# If it does not exist, return -1.

# tips:
# 用dict累計出現次數

# blind spot:
# 因為英文只有26字母，空間複雜度是O(1)不是O(1)

class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        counter = {}
        
        for char in s:
            counter[char] = counter.get(char, 0) + 1

        for idx, char in enumerate(s):
            if counter.get(char) == 1:
                return idx
        
        return -1