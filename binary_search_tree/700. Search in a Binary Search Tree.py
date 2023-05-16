# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# 遞迴解
# 提示: 遞迴的input跟searchBST相同，不用建立helper函數
class Solution(object):
    def searchBST(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """
        if not root: return None  # 節點不存在，則無解
        if root.val > val:
            return self.searchBST(root.left, val)  # 節點值大於目標值，往左子樹找
        elif root.val < val:
            return self.searchBST(root.right, val)  # 節點值小於目標值，往右子樹找
        else:
            return root  # 找到目標值，回傳節點(子樹)

# 迭代解
class Solution(object):
    def searchBST(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """

        pointer = root  # 利用pointer走訪樹
        while pointer:
            if not pointer: return None
            if pointer.val == val:
                return pointer
            elif pointer.val > val:
                pointer = pointer.left
            else:
                pointer = pointer.right

        return None


# second try:用inorder找val
class Solution(object):
    def searchBST(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """
        if not root:
            return None

        left = self.searchBST(root.left, val)
        if left:
            return left

        if root.val == val:
            return root
        
        right = self.searchBST(root.right, val)
        if right:
            return right

        return None

# second try:
class Solution(object):
    def searchBST(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """
        p = root
        while p:
            if not p:
                return None
            
            if p.val > val:
                p = p.left
            elif p.val < val:
                p = p.right
            else:
                return p

        return None
            