# Given an integer array nums where the elements are sorted in ascending order, convert it to a 
# height-balanced binary search tree.

# tips:
# 在嚴格遞增數列中，取中位數，左邊一定比中位數小，可為左子樹，右邊一定比中位數大，可為右子樹
# 建立createNode函數遞迴的取中位數並生成節點與左右子樹
# 記得有停止條件lower> upper

# first try
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
        
        