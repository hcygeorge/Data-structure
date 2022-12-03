# Given a binary array nums, return the maximum number of consecutive 1's in the array.
class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        max_ones = 0
        counter = 0
        for i in nums:
            if i == 1:
                counter += 1
            else:
                if counter > max_ones:
                    max_ones = counter
                counter = 0
        if counter > max_ones:
            max_ones = counter
        return max_ones