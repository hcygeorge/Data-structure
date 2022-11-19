# Third Maximum Number

# 直覺解法，先排序再找第三大元素，O(nlogn)
class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        # sort array
        nums = sorted(nums, reverse=True)
        
        # count unique elements and save previous element
        counter = 0
        prev = None  # in order to find duplicated element
        
        # iterate on sorted array to find the third max, stop when counter == 3
        for idx in range(len(nums)):
            if idx == 0:
                counter += 1
                prev = nums[idx]

            if nums[idx] != prev:
                counter += 1
                prev = nums[idx]

            if counter == 3:
                break   
        
        # if counter == 3, return third max, else return max
        if counter == 3:
            return nums[idx]
        else:
            return nums[0]
        
# O(n)解法