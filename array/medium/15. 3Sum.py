# tips: Fix one pointer first and the problem turn into 2Sum
# Sort the nums in order to use left-right pointer and skip the same values
# The time complexity is O(n^2), space complexity is O(1)
# attempt count: 1

# blind spots: forget to skip same value of nums[i], right - 1

# 1st try, 2nd try
class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        res = []
        
        for i in range(len(nums) - 2):  # keep 2 elements for left and right
            if i > 0 and nums[i] == nums[i-1]:
                continue
                
            left = i + 1
            right = len(nums) - 1
            
            while left < right:
                total = nums[i] + nums[left] + nums[right]
                if total > 0:
                    right -= 1
                elif total < 0:
                    left += 1
                else:
                    res.append([nums[i], nums[left], nums[right]])
                    
                    # skip the same values before moving pointers
                    while left < right and nums[left+1] == nums[left]:
                        left += 1
                    while left < right and nums[right-1] == nums[right]:  # note that right-1
                        right -= 1
                
                    left += 1
                    right -= 1
                    
        return res
                    