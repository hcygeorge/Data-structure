# tips: 往左右子樹遞迴以累計相同值的路徑長度
# 假設該節點是路徑最上層的節點
# 則該節點長度為左子樹加上右上子樹回傳的長度(值不一樣時子樹回傳長度為0)
# 若長度為當下最長則更新self.mx
# 若該節點還不是路徑中最上層的節點，該路徑最長長度後續會被更新
class Solution(object):
    def __init__(self):
        self.mx = 0
    def longestUnivaluePath(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        
        self.dfs(root, root.val)

        return self.mx

    def dfs(self, node, val):
        if not node:
            return 0
        
        l = self.dfs(node.left, node.val)
        r = self.dfs(node.right, node.val)

        self.mx = max(self.mx, l+r)

        if node.val == val:
            return max(l, r) + 1
        else:
            return 0