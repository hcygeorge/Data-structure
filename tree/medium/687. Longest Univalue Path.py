# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def __init__(self):
        self.mx = 0
    def longestUnivaluePath(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        
        self.dfs(root, root.val)

        return self.mx

    def dfs(self, node, val):
        if not node:
            return 0
        
        l = self.dfs(node.left, node.val)
        r = self.dfs(node.right, node.val)

        self.mx = max(self.mx, l+r)

        if node.val == val:
            return max(l, r) + 1
        else:
            return 0