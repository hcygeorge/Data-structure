# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# tips:
# 平衡的定義是左右子樹的高度差不大於1
# 建立check(root)遞迴的計算每個子樹高度，如果該樹或該樹的左右子樹不平衡，則回傳-1代表不平衡
# 否則回傳該子樹的高度，包括節點自己加上左右子樹最高的那一個，1+max(left, right)
# 呼叫並判斷check(root)的結果是否為-1

# blind spot:
# 有時會想不到怎麼計算高度，高度算法是節點本身(1)加上子樹高度，return 1 + check_depth(subrtree)
# 檢查高度差應該放在輔助函數內，否則只會比較root兩子樹的高度差
# 高度差大於1時要回傳-1代表不平衡，回傳False會被當成0，回傳非數字會導致abs(l-r)出錯
# 只要其中一次遞迴回傳-1，整個函數就一定回傳-1

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


# second try: 方法與上次相同
class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        
        def check_depth(root):
            if root == None:
                return 0
            
            left = check_depth(root.left)
            right = check_depth(root.right)

            if left == -1 or right == -1 or abs(left - right) > 1:
                return -1

            return 1 + max(left, right)
        
        return check_depth(root) != -1

# third try:
class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        
        return self.depth(root) != -1
    
    def depth(self, node):
        if not node:
            return 0

        left = self.depth(node.left)
        right = self.depth(node.right)

        if abs(left - right) > 1 or left == -1 or right == -1:
            return -1

        return 1 + max(left, right)