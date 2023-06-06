# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# 提示:
# 這題麻煩在怎麼走訪時怎麼判斷和紀錄節點屬於哪一層
# 可以建立變數level負責記錄層數，再根據level索引儲存在res中第幾個list
# 建立輔助函數，參數為走訪的node、儲存node值的res(list of list)、與node的層數level
# level可用於判斷何時在res內新增一層，走訪樹時根據層級將元素加入對應list
# 遞迴時以一個counter紀錄元素在第幾層
# 迭代時則以counter紀錄該層有幾個元素，以用來決定對deque的迭代次數，到下一層時再重新計算

# blind spot:
# queue長度代表該層長度，利用queue長度決定要迭代幾次，可確保每一層元素都存在同一個陣列內

# 遞迴解
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        res = []
        if not root: return res
        res.append([])

        def helper(node, res, level):
            if not node: return res
            if level > len(res) - 1:
                lvl = [node.val]
                res.append(lvl)
            else:
                res[level].append(node.val)

            helper(node.left, res, level+1)
            helper(node.right, res, level+1)

        helper(root, res, 0)

        return res
    
# 迭代解
from collections import deque

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root: return None
        res = []
        q = deque([root])

        while q:
            counter = len(q)  # 計算該層的節點個數
            level = []
            for _ in range(counter):
                node = q.popleft()
                level.append(node.val)

                # 將下一層的節點先放入queue，等下次迭代再處理
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            res.append(level)

        return res
    

# second try: 迭代解，因為有記錄level，所以不用先計算節點個數決定迭代個數，也可用stack取代deque
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []

        stack = [(0, root)]  # 同時記錄level
        res = []

        while stack:
            level, node = stack.pop()

            if not node:
                continue

            if level > len(res) - 1:
                res.append([node.val])
            else:
                res[level].append(node.val)

            stack.append((level+1, node.right))  # stack先進後出
            stack.append((level+1, node.left))

        return res
    
# third try: 遞迴解，把輔助函數獨立出來，解題邏輯不變
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        res = []
        level = 0

        return self.traversal(root, res, level)

    def traversal(self, node, res, level):
        if not node:
            return res
        
        if level + 1 > len(res):
            res.append([node.val])
        else:
            res[level].append(node.val)
        
        self.traversal(node.left, res, level+1)
        self.traversal(node.right, res, level+1)

        return res