# tips: 可以用level的奇偶判斷要該level要順著走還是反著走
# 可以在走訪時根據走向決定要將元素插入在前面或後面，或是全部走訪完再反轉奇數level
# 下次做要想迭代解


class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        level = 0
        res = []

        def traverse(node, level):
            if not node:
                return None
            
            if len(res) < level+1:
                res.append([node.val])
            else:
                if level % 2 == 1:
                    res[level].insert(0, node.val)
                else:
                    res[level].append(node.val)
            
            traverse(node.left, level+1)
            traverse(node.right, level+1)
            
        traverse(root, 0)
        
        # for level in range(len(res)):
        #     if level % 2 == 1:
        #         res[level] = reversed(res[level])
        
        return res
    
class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        level = 0
        res = []

        def traverse(node, level):
            if not node:
                return None
            
            if len(res) < level+1:
                res.append([node.val])
            else:
                res[level].append(node.val)
            
            traverse(node.left, level+1)
            traverse(node.right, level+1)
            
        traverse(root, 0)
        
        for level in range(len(res)):
            if level % 2 == 1:
                res[level] = reversed(res[level])
        
        return res