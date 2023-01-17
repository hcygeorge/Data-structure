# Given the root of a binary tree, return the inorder traversal of its nodes' values.

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# inorder: 左根右
# 1.遞迴到最底下的左子樹後取得值
# 2. 走回上一層取得其根節點的值
# 3. 然後走到右子樹，以右子樹為根檢查1, 2
# 4. 1,2都做完才取右子樹值

# Recursion solution
class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        self.res = []
        def inorder(root):
            if not root: return None
            if root.left:
                inorder(root.left)
            self.res.append(root.val)
            if root.right:
                inorder(root.right)

        inorder(root)

        return self.res