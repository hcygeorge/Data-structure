

# first try: it will exceed time limit when the input array is large
class Solution(object):
    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        j = 1
        while j < len(nums) - 1:
            # find i
            i = j - 1
            print(i)
            while nums[i] >= nums[j]:
                if i > 0:
                    i -= 1
                else:
                    break
            # find k
            k = j + 1
            while nums[j] >= nums[k]:
                if k < len(nums)-1:
                    k += 1
                else:
                    break
            if nums[i] < nums[j] and nums[j] < nums[k]:
                return True
            j += 1
        return False
    

class Solution(object):
    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        num_i, num_j = float('inf'), float('inf')
        
        for d in nums:
            if d <= num_i:
                num_i = d
            elif d <= num_j:
                num_j = d
            else:
                return True
            
        return False