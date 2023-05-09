# Given the root of a binary tree, return its maximum depth.
# A binary tree's maximum depth is the number of nodes along the longest path
# from the root node down to the farthest leaf node.

# tips:
# 檢查root存在與否
# 建立check函數遞迴的檢查node是否存在並計算深度，node深度為自己1+max(左子樹, 右子樹)深度

# first try: recursion solution
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root == None:
            return 0
        if (root.left or root.right) == None:
            return 1
        
        def check(node):
            if not node:
                return 0
            
            left = check(node.left)
            right = check(node.right)
            
            return 1 + max(left, right) 
        
        return check(root)