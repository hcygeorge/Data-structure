# Given an integer array nums, 
# move all 0's to the end of it while maintaining the relative order of the non-zero elements.

# 題目要求inplace，想到left right pointers
# 慢指針負責指著最後一個0值等著與後面交換
class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        fast = 0
        slow = 0

        while fast < len(nums):
            if nums[fast] == 0:
                fast += 1
                # 遇到0時，slow停著等著與後面的非0值交換
            else:
                if fast != slow:  # 這是多餘的檢查，因為即使一樣交換也不影響結果
                    nums[fast], nums[slow] = nums[slow], nums[fast]
                fast += 1
                slow += 1  # 交換完畢，可以指向下一個值

# 第二次解
class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        
        p1 = 0
        p2 = 0  # 負責指著最後一個經到的0，等到p1走道非0後交換

        while p1 < len(nums):
            if nums[p1] == 0:
                p1 += 1
            else:
                nums[p1], nums[p2] = nums[p2], nums[p1]
                p1 += 1
                p2 += 1