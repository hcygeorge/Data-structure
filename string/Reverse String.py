# Write a function that reverses a string. The input string is given as an array of characters s.
# You must do this by modifying the input array in-place with O(1) extra memory.
class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        # 2 pointers from opposite direction
        left = 0
        right = len(s) - 1
        
        # iterate on both side of string
        while left < right: 
            # exchange left element and right element
            s[left], s[right] = s[right], s[left]
            
            # move pointers
            left += 1
            right -= 1