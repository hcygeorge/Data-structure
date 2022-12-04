# Given an integer array nums, 
# move all 0's to the end of it while maintaining the relative order of the non-zero elements.

# use 2 pointers
# 注意慢指針p2和p1同時前進，直到遇到0為止
class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        
        p1 = 0
        p2 = 0
        
        while p1 < len(nums):
            if nums[p1] == 0:
                p1 += 1
            else:
                if p1 != p2:
                    nums[p1], nums[p2] = nums[p2], nums[p1]
                p1 += 1
                p2 += 1
                