# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# tips:
# 遞迴解
# 1. 檢查p,q是否存在
# 2. 檢查p,q值是否相等
# 3. 若相等則再遞迴兩者的left,right
# 迭代解
# 將p,q存入queue中(先進先出)，對queue迭代，
# 每次檢查完都先將p,q的左右子樹存入deque，以便繼續檢查

# blind spot:
# 注意在迭代解時，一個not p and not q時不代表整棵樹相同，因此不能直接回傳True，需要跳過該次迭代(continue)

# attempt count: 5

class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        if not p and not q: return True
        if not p or not q: return False
        return p.val == q.val and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)


# 思路: 將p,q存入deque中，對deque迭代，每次檢查完都先將p,q的左右子樹存入deque，以便繼續檢查
from collections import deque
class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """

        d = deque([(p, q)])  # 雙向佇列，可以popleft()

        while d:
            p, q = d.popleft()

            # 確認存在性
            if not p and not q:
                continue  # 注意這裡跟遞迴解不一樣!
            if not p or not q:
                return False

            # 檢查值是否相同
            if p.val == q.val:
                # 將下次要檢查的node排入deque
                d.append((p.left, q.left))
                d.append((p.right, q.right))
            else:
                return False
        # 通過全部檢查，代表兩樹相同
        return True
