# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# 遞迴解
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


# 迭代解
from collections import deque
class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root: return True
        q = deque([(root.left, root.right)])
        while q:
            l, r = q.popleft()
            if not l and not r:
                continue
            if l and r and l.val == r.val:
                q.append((l.left, r.right))
                q.append((l.right, r.left))
            else:
                return False
        return True
            