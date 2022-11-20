# Third Maximum Number

# 其他解法
# Min Heap Data Structure，O(n)
# Sorted set，O(n)

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

# 3 Pointers
# O(n)
# flag用於判斷變數是否有更新，避免遇到元素剛好等於預設值的情況
class Solution:
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Tuples to store number and show if the number is updated
        first = (0, False)
        second = (0, False)
        third = (0, False)
        
        # Iterate on nums and updated tuples
        for num in nums:
            # skip num if it is already exist
            if (first[1] and num == first[0]) or \
                (second[1] and num == second[0]) or \
                (third[1] and num == third[0]):
                continue
            
            # if num > first
            if first[1] == False or num >= first[0]:
                third = second
                second = first
                first = (num, True)
            
            # elif num > second
            elif second[1] == False or num >= second[0]:
                third = second
                second = (num, True)
            # elif num > third
            elif third[1] == False or num >= third[0]:
                third = (num, True)
            
        # return third if updated
        if not third[1]:
            return first[0]
            
        return third[0]