# Squares of a Sorted Array
class Solution:
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        l = len(nums)
        left = 0
        right = l - 1
        output = [0] * l
        idx = l - 1  # 注意此位置從最後往前排
        
        while left <= right:
            if abs(nums[left]) < abs(nums[right]):
                output[idx] = nums[right] ** 2
                right -= 1
            else:
                output[idx] = nums[left] ** 2
                left += 1
            idx -= 1
        
        return output
