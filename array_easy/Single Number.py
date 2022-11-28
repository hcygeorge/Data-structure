# Single Number
# Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.
# You must implement a solution with a linear runtime complexity and use only constant extra space.

# 暴力解: 遍歷每個數字並比較是否與其他數字與重複，O(n^2), O(1)
# 先排序後比對: O(nlogn), O(n)
# Hashmap累計出現次數: O(n), O(n)
# Bitwise Operation: O(n), O(1), refer to https://ithelp.ithome.com.tw/articles/10213278?sc=pt

class Solution(object):
    """
    用Hashmap累計元素出現次數，找出只出現一次的元素
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
            
class Solution2(object):
    """
    Bitwise operation
    use XOR to eliminate duplicate number and retain the unique one.
    """
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = nums[0]
        
        for i in range(1, len(nums)):
            res ^= nums[i]
            
        return res