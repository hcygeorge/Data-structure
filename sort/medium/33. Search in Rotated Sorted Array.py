# 當mid大於最右邊的值，代表mid右半邊是有排序的，
# 此時只能檢查mid<target<upper確定target是否落在右半邊，反之target落在左半邊
# 若mid小於最右邊的值，則代表mid左半邊有序，
# 只能檢查mid<target<upper確定target是否落在左半邊，然後縮小範圍
# 注意改成檢查mid與最左邊的值會出錯，因為mid可能剛好是lower，在[3,1]時出錯
class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        lower, upper = 0, len(nums)-1
        
        while lower <= upper:
            mid = (lower + upper) // 2
            
            if nums[mid] == target:
                return mid

            if nums[mid] < nums[upper]:
                # target must be compared with the upper bound because the upper bound may not be the maximum value
                if target > nums[mid] and target <= nums[upper]:
                    lower = mid + 1
                else:
                    upper = mid - 1
            else:
                # target must be compared with the lower bound because the lower bound may not be the mininum value
                if target < nums[mid] and target >= nums[lower]:
                    upper = mid - 1
                else:
                    lower = mid + 1
        
        return -1
            