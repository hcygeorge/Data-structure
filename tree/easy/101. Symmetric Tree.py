# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root: return True

        return self.isSym(root.left, root.right)
        
    def isSym(self, l, r):
        if not l and not r: return True
        if not l or not r: return False
        if l.val != r.val: return False

        return self.isSym(l.right, r.left) and self.isSym(l.left, r.right)




