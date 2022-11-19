# Height Checker
# TC: O(nlogn)
# SC: O(n)

class Solution(object):
    def heightChecker(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        
        # sort array O(nlogn)
        sorted_height = sorted(heights)
        
        # compare 2 arary O(n)
        counter = 0
        for idx in range(len(heights)):
            if sorted_height[idx] != heights[idx]:
                counter += 1
        
        return counter

