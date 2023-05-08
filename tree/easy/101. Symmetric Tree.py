# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# tips:
# 對稱樹代表每個左子樹的左樹會等於右子樹的右樹，且左子樹的右樹會等於右子樹的左樹
# 建立函數isSym遞迴檢查樹的對稱性
# 或是用deque將被檢查的節點對先儲存，再以先進先出的方式逐個檢查值是否相等
# 注意迭代時一對left, right都不存在不代表整顆樹對稱，要繼續檢查到deque為空

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


# second try: 遞迴解，邏輯與上次相同，但可讀性比較好
class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        
        def isSym(left, right):
            if not left and not right:
                return True
            if not left or not right:
                return False

            l = isSym(left.left, right.right)
            r = isSym(left.right, right.left)

            if left.val != right.val or not l or not r:
                return False

            return True

        return isSym(root.left, root.right)
    
# second try: 迭代解，邏輯與上次相同
from collections import deque
class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        q = deque([(root.left, root.right)])

        while q:
            left, right = q.popleft()
            if not left and not right:
                continue
            if (not left or not right) or left.val != right.val:
                return False

            q.append((left.left, right.right))
            q.append((left.right, right.left))

        return True