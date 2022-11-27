# Single Number
# Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.
# You must implement a solution with a linear runtime complexity and use only constant extra space.

# 暴力解: 遍歷每個數字並比較是否與其他數字與重複，O(n^2), O(1)
# 先排序後比對: O(nlogn), O(n)
# Hashmap累計出現次數: O(n), O(n)
# Bitwise Operation

class Solution(object):
    """
    Hashmap累計出現次數
    """
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # create hash map of nums
        hash_map = dict(zip(nums, [0]*len(nums)))
        
        # count item frequency
        for ele in nums:
            hash_map[ele] += 1
        
        # return item that occurred only once
        for ele, count in hash_map.items():
            if count == 1:
                return ele