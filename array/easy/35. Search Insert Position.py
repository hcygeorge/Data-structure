# Search Insert Position

# 提示
# 使用binary search
# 迭代條件必須包括lo=up
# 當lo=up時，若仍未找到值，則lo會被加1，此時lo就是插入新值的位置
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



