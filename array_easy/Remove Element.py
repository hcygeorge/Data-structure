# Given an integer array nums and an integer val, remove all occurrences of val in nums in-place. The relative order of the elements may be changed
# hints
# 元素順序無所謂
# 只用單紙張將元素與下個元素交換位置，將無法判斷移除後array的長度
# 用快指針找到該留著的元素，移動元素到慢指針

# 用快慢指針解
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
    
# 用對撞指針解
class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        length = len(nums)
        left = 0
        right = length
        
        while left < right:
            if nums[left] == val:
                nums[left] = nums[right-1]
                right -= 1
            else:
                left += 1
        
        print(right, nums)
        return right            
