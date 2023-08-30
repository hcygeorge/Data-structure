# 排序陣列中找值，先想到二元搜尋法

# 找到目標值後，再從左右逐一搜尋目標範圍，複雜度n+logn=O(n)
class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        if not nums:
            return [-1, -1]
        
        lower, upper = 0, len(nums)-1
        
        while lower <= upper:
            mid = (lower+upper) // 2
            
            if nums[mid] == target:
                left, right = mid, mid
                
                while left-1 >= 0:
                    if nums[left-1] == target:
                        left -= 1
                    else:
                        break
                while right+1 < len(nums):
                    if nums[right+1] == target:
                        right += 1
                    else:
                        break
                
                return [left, right]
            
            elif nums[mid] > target:
                upper = mid-1
            elif nums[mid] < target:
                lower = mid+1
                
        return [-1, -1]
    
# 做兩次二元搜尋，分別找上下範圍，O(logn)
class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        if not nums:
            return [-1, -1]
        

        def binary_search(bound):
            lower, upper = 0, len(nums)-1
            
            while lower <= upper:
                mid = (lower+upper) // 2
                
                if nums[mid] == target:
                    if bound == 'left':
                        upper = mid-1
                    elif bound == 'right':
                        lower = mid+1

                elif nums[mid] > target:
                    upper = mid-1
                elif nums[mid] < target:
                    lower = mid+1

            if bound == 'left':
                return lower
            elif bound == 'right':
                return upper
                    
        left, right = binary_search('left'), binary_search('right')
        return [left, right] if left <= right else [-1, -1]