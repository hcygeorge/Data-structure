# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

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

        # 用同樣邏輯檢查並合併左子樹與柚子數
        root1.left = self.mergeTrees(root1.left, root2.left)
        root1.right = self.mergeTrees(root1.right, root2.right)

        return root1