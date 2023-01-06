# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def check(root):
            if root == None:
                return 0
            l = check(root.left)
            r = check(root.right)

            if abs(l - r) > 1 or l == -1 or r == -1:
                return -1

            return 1 + max(l,r)
        
        return check(root) != -1
