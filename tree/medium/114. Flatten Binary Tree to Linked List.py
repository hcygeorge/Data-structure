# tip1: 用dfs走訪節點，每次先攤平左子樹，接到右子樹上，然後再接上攤平的右子樹
# tip2: 用prev左訪節點，prev永遠在接上子樹後的最尾端

class Solution(object):

    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: None Do not return anything, modify root in-place instead.
        """
        self.dfs(root)
    
    def dfs(self, node):
        if not node:
            return None
        
        l = node.left
        r = node.right

        self.dfs(l)
        self.dfs(r)

        node.left = None
        node.right = l
        while node.right:
            node = node.right

        node.right = r

class Solution(object):

    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: None Do not return anything, modify root in-place instead.
        """
        if not root:
            return None

        self.prev = root
        self.flatten(root.left)
        r = root.right

        root.right = root.left
        root.left = None
        self.prev.right = r
        self.flatten(r)