# tips: 若該點是"最低"共同祖先，則p,q可能情況是:
# 一個在根，一個在左或右其中之一
# 兩個分別在左右子樹
# 我們用l, r, mid變數為1表示是否包含p,q
# 若l+r+mid=2表示為最低共同祖先，更新self.lca
# 若為非最低的共同祖先，代表p,q同時在左子樹或同時在右子樹，此時l+r+mid=1

class Solution(object):
    def __init__(self):
        self.lca = None
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        self.dfs(root, p, q)
        return self.lca


    def dfs(self, node, p, q):
        if not node:
            return False

        l = 1 if self.dfs(node.left, p, q) else 0
        r = 1 if self.dfs(node.right, p, q) else 0

        if node == p or node == q:
            mid = 1
        else:
            mid = 0

        if l + r + mid == 2:
            print(node.val)
            self.lca = node

        return l + r + mid > 0
