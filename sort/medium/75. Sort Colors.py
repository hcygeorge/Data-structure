# tips: use counting sort, which means count the number of each digit, and then overwrite the array.

from collections import OrderedDict
class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        counter = OrderedDict({0: 0, 1: 0, 2: 0})
        
        for i in nums:
            counter[i] += 1
        
        init = 0
        for k, v in counter.items():
            if v != 0:
                for j in range(init, init+counter[k]):
                    nums[j] = k

                init += counter[k]
            
            
            