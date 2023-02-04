# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# 遞迴解
# 提示: 用inorder走訪BST，必會得到嚴格遞增的陣列
class Solution(object):
    def __init__(self):
        self.last = -float('inf')  # 用於檢查節點值是否大於前一個節點值
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True

        if not self.isValidBST(root.left):  # 左子樹不是BST，則母樹也不是BST
            return False

        if root.val <= self.last:
            return False
        else:
            self.last = root.val
        
        return self.isValidBST(root.right)  # 移動到右子樹
