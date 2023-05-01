# Search Insert Position

# tips
# 使用binary search
# 迭代條件必須包括lo=up
# 當lo=up時，若仍未找到值，則lo會被加1，此時lo就是插入新值的位置

# first try
class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        lo = 0
        up = len(nums) - 1

        while lo <= up:
            mid = (lo + up) // 2
            if target > nums[mid]:
                lo = mid + 1
            elif target < nums[mid]:
                up = mid - 1
            else:
                return mid
        
        return lo

# second try
class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        lower, upper = 0, len(nums) - 1

        while lower <= upper:
            mid = (lower + upper) // 2
            if nums[mid] < target:
                lower = mid + 1
            elif nums[mid] > target:
                upper = mid - 1
            else:
                return mid
        
        return lower


