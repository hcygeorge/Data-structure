# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# 提示:
# 不用一次收集完同一層的元素，而是先建立每層專用的list，走訪樹時根據層級將元素加入對應list
# 遞迴時以一個counter紀錄元素在第幾層
# 迭代時則以counter紀錄該層有幾個元素，以用來決定對deque的迭代次數，到下一層時歸零重新計算

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