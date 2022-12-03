# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
# You can return the answer in any order.


# Brute Force
# O(n^2)
class Solution():
    def twoSum(self, num, target):
        for i in range(len(num)):
            for j in range(i+1, len(num)):
                if num[i] + num[j] == target:
                    return [i, j]
                
# Hash Map
# O(n)
# 注意若先將資料放進hash table，則必須檢查是否一筆資料與自己相加
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        num_map = {}
        
        for i in range(len(nums)):
            if target - nums[i] in num_map:
                return [num_map[target - nums[i]], i]
            
            if nums[i] not in num_map:
                num_map[nums[i]] = i
            