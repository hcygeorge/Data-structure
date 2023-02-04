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

# 迭代解
# 提示: 利用stack先收集所有左節點
# pre代表前一個節點，curr為現在走道的節點
class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root: return True
        stack = []
        pre = None
        curr = root
        while curr or stack:  # stack沒有了只表示節點的左子樹走訪完，但curr裡可能還有右子樹
            while curr:  # 先將所有左節點加入stack
                stack.append(curr)
                curr = curr.left

            curr = stack.pop()

            if pre and curr.val <= pre.val:
                return False
            pre = curr
            curr = curr.right
        
        return True
