# Given the root of a binary tree, return the inorder traversal of its nodes' values.

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# tips: inorder(中序)走訪順序為左中右
# 1. 遞迴到最底下的左子樹後取得值
# 2. 走回上一層取得其根節點的值
# 3. 然後走到右子樹，以右子樹為根檢查1, 2
# 4. 1,2都做完才取右子樹值

# blind spot:
# 迭代解時記得要建立一個curr走訪左子樹，走到底才開始取左中右值

# attempt count: 4

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
    
# Iteration Solution
# 建立res, stack
# 1. cur從root開始，先一直往左子樹走，並將節點放入stack
# 2. 走到底(左子樹不存在)後把stack的節點挑出來(後進的先出)，節點值加入res
# 3. 走到右子樹，若右子樹存在則會回到1,2(往它的左子樹走)
# 4. 若右子樹不存在，檢查條件會從stack挑出上一個左子樹(回到2)
# 5. 重複以上步驟直到cur和stack都空了
class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res = []
        stack = []  # LIFO
        cur = root
        while cur or stack:
            if cur:
                stack.append(cur)
                cur = cur.left
            else:
                cur = stack.pop()
                res.append(cur.val)
                cur = cur.right  # if right is null, then it will check cur's root from stack next round
        
        return res
    

# 2nd try: recursion solution
class Solution(object):
    def inorder(self, root, res):
        if not root:
            return None

        self.inorder(root.left, res)
        res.append(root.val)
        self.inorder(root.right, res)
        
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res = []
        self.inorder(root, res)

        return res

# 4th try: recursion solution
class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res = []

        def traverse(node):
            if not node:
                return None
            
            traverse(node.left)
            res.append(node.val)
            traverse(node.right)

        traverse(root)

        return res
