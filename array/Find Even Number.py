# Given an array nums of integers, return how many of them contain an even number of digits.
class Solution(object):
    def findNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        counter = 0
        for i in nums:
            if len(str(i))%2 == 0:
                counter += 1
        return counter
            