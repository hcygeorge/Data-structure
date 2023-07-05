# tips: use counting sort, which means count the number of each digit, and then overwrite the array with ordered digits.
# 用指針時要注意把交換p跟r的數字後，指針p須留在原處檢查新數字是否為0
# counting sort缺點是沒有穩定性
class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        counter = [0, 0, 0]  # idx represents the digit
        
        # count digit
        for i in nums:
            counter[i] += 1
        
        # replace digit in-place
        init = 0
        for num in range(3):
            if counter[num] != 0:
                for j in range(init, init+counter[num]):
                    nums[j] = num

                init += counter[num]
            
class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        l = 0
        r = len(nums) - 1
        p = 0

        while p <= r:
            if nums[p] == 2:
                nums[p], nums[r] = nums[r], nums[p]
                r -= 1
            elif nums[p] == 0:
                nums[p], nums[l] = nums[l], nums[p]
                l += 1
                p += 1
            else:
                p += 1

            
            