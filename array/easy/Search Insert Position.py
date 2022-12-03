# Search Insert Position
# use binary search
# if target not exist, insert data at lo
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
            mid = (lo+up)//2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                lo = mid + 1
            else:
                up = mid - 1
        
        return lo