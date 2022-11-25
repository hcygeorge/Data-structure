# Rotate Array
# Given an array, rotate the array to the right by k steps, where k is non-negative.
# do it in-place
# 將陣列顛倒後，再將前k個元素和後len(nums)-k的元素分別顛倒，即可得到往右移動k步的答案
class Solution(object):

    
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        l = len(nums)
        k = k % l  # 重要，避免k>=l的情況，此時移動k步會index out of range或錯置
        
        # edge case: k = 0
        if k == 0:
            return None
        
        def reverse(left, right):
            while left < right:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1
                
        # reverse the whole array
        reverse(0, l-1)
        # reverse first k array
        reverse(0, k-1)
        # reverse last k array
        reverse(k, l-1)   
            
# non in-place
# 直接將後k項和前l-k項合併起來(l為陣列長度)，
# 將整個陣列重複銜接一次，取[(l-k):(2 * l - k)]亦可。

# refer to
# https://ithelp.ithome.com.tw/articles/10213291