# Contains Duplicate
# 將array存在set(hash table)用於檢查是否重複
# TC: O(n), SC: O(n)
# 另種解法是先排序陣列，再比較元素是否與相鄰者重複，複雜度取決於排序方法，如Timsort
# TC: O(nlogn), SC: O(n)
class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # create a set of nums
        checked = set()
        
        # iterate on nums
        for ele in nums:
            if ele in checked:  # check if element exists in the set
                return True
            else:  # or add element into the set
                checked.add(ele)
        
        # return False if no duplicate element exists
        return False
