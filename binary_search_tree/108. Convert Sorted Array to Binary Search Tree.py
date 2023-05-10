# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if len(nums) == 1:
            return TreeNode(nums[0])
        
        return self.createNode(nums, 0, len(nums)-1)
    
    def createNode(self, nums, lower, upper):
        if lower > upper:
            return None
        
        mid = (lower + upper) // 2
        
        node = TreeNode(nums[mid])
        node.left = self.createNode(nums, lower, mid-1)
        node.right = self.createNode(nums, mid+1, upper)
        
        return node
        
        