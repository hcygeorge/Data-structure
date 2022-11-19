# https://leetcode.com/explore/learn/card/fun-with-arrays/511/in-place-operations/3258/
# hint1 元素必須緊密排列，因此無法只用單指針遍歷，需要使用快慢指針
class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l = len(nums)
        fast = 0
        slow = 0
        unique_counter = 0
        
        while fast <= l-1:
            if fast == 0:
                slow += 1
                unique_counter += 1
            else:
                if nums[fast] != nums[fast-1]:
                    nums[slow] = nums[fast]
                    slow += 1
                    unique_counter += 1
                    
            fast += 1
        return unique_counter