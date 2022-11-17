# Given an integer array nums and an integer val, remove all occurrences of val in nums in-place. The relative order of the elements may be changed
# hints
# 元素順序無所謂
# 直接交換元素位置會覆蓋到下個元素，而且無法判斷最後array的長度
# 用快指針找到該留著的元素，移動元素到慢指針
class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        length = len(nums)
        fast = 0
        slow = 0
        
        while fast < length:
            if nums[fast] != val:
                nums[slow] = nums[fast]
                slow += 1
            fast += 1
        
        return slow