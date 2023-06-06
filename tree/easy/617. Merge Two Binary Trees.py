# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# tips:
# 先檢查root1, root2存在性
# 遞迴解: 將root2.val加到root1.val，遞迴的對left, right做一樣的事情
# 迭代解: 將root1和root2加到stack，再走訪stack將root2.val加到root1.val，將left, right加入stack

# blind spot:
# 記得遞迴函數要回傳給root左右子樹
# 注意每次迭代先檢查root2是否存在，再檢查root1，只知道其中一個不存在無法決定處理方法
# 當root1為None，root1=root2無法改變root1，必須在上一次迭代用(父節點存在)root1.left = root2.left

# 遞迴解
class Solution(object):
    def mergeTrees(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: TreeNode
        """  
        if not root1 and not root2:  # 都不存在
            return None
        if not root1 or not root2:  # 只有其中一個存在，用存在的那個
            return root1 or root2
        
        root1.val = root1.val + root2.val  # 都存在，合併值於第一棵樹

        # 用同樣邏輯檢查並合併左子樹與右子樹
        root1.left = self.mergeTrees(root1.left, root2.left)
        root1.right = self.mergeTrees(root1.right, root2.right)

        return root1
    
# 迭代解
class Solution(object):
    def mergeTrees(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: TreeNode
        """
        # 檢查root1, root2是否存在
        if not root1 and not root2:
            return None
        if not root1 or not root2:
            return root1 or root2
        
        # 也可以只檢查root1，root2是否存在留到後面while再檢查
        # if not root1:
        #     return root2
        
        stack = []
        stack.append((root1, root2))

        while stack:
            t = stack.pop()
            # 若t[1](root2)不存在不用合併
            if not t[1]:
                continue
            # 以t[0](root1)為主體合併root2
            t[0].val += t[1].val

            # 同樣邏輯，先檢查root1子樹是否存在，若存在則加入stack做合併
            if not t[0].left:
                t[0].left = t[1].left
            else:
                stack.append((t[0].left, t[1].left)) 
            # 同樣邏輯，先檢查root2子樹是否存在，若存在則加入stack做合併
            if not t[0].right:
                t[0].right = t[1].right
            else:
                stack.append((t[0].right, t[1].right)) 
        
        # 返回合併的root1
        return root1

# second try: same as before
class Solution(object):
    def mergeTrees(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: TreeNode
        """
        # deal with 0 node
        if not root1 and not root2:
            return None
        if not root1 or not root2:
            return root1 or root2

        # sum up overlap node value
        root1.val += root2.val
        root1.left = self.mergeTrees(root1.left, root2.left)
        root1.right = self.mergeTrees(root1.right, root2.right)

        return root1
    
# second try:
from collections import deque
class Solution(object):
    def mergeTrees(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: TreeNode
        """
        if not root1 and not root2:
            return None
        if not root1 or not root2:
            return root1 or root2

        queue = deque([(root1, root2)])

        while queue:
            l, r = queue.popleft()

            if not r:
                continue

            l.val += r.val
            
            if l.left:
                queue.append((l.left, r.left))
            else:
                l.left = r.left

            if l.right:
                queue.append((l.right, r.right))
            else:
                l.right = r.right

        return root1


