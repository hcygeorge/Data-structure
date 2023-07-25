
# brute forced solution
class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        p = 0
        
        if len(nums) == 1:
            return p
        
        while p < len(nums):
            if p == 0 and nums[p] > nums[p+1]:
                return p
            elif p == len(nums) - 1 and nums[p] > nums[p-1]:
                return p
            else:
                if nums[p] > nums[p+1] and nums[p] > nums[p-1]:
                    return p
            
            p += 1
            
        return None
            
# utilize binary search process to run in O(logn)
class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left = 0
        right = len(nums) - 1

        while left < right - 1:
            mid = (left + right) // 2

            if nums[mid] > nums[mid-1] and nums[mid] > nums[mid+1]:
                return mid

            if nums[mid] < nums[mid+1]:
                left = mid + 1
            else:
                right = mid - 1
        
        return left if nums[left] >= nums[right] else right
