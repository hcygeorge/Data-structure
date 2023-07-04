# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# tips:
# 利用self.isValidBST(root.left)遞迴的走到最底部的左子樹
# 或建立curr迭代的將節點放入stack

# blind spot:
# 右子樹等所有左子樹遞迴完才檢查
# 犯了一個錯是想把左子樹右子樹的遞迴結果留到return時判斷
# 這樣不符合inorder得執行順序

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

        # 會一直往左走到底
        if not self.isValidBST(root.left):  # 左子樹不是BST，則母樹也不是BST
            return False

        # 從左邊最底部開始往回走，值應該要越來越大
        if root.val <= self.last:
            return False
        else:
            self.last = root.val
        
        return self.isValidBST(root.right)  # 移動到右子樹

# 迭代解
# 提示: 利用stack先收集所有左節點
# pre代表前一個節點，curr為現在的節點
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


# 迭代解
# 用continue就可以利用一個迴圈走訪左子樹
class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        last = -float('inf')
        if not root:
            return True
        stack = []
        curr = root

        while curr or stack:
            if curr: # 這裡檢查curr而不是curr.left
                stack.append(curr)
                curr = curr.left
                continue
            else:
                curr = stack.pop()
                if curr.val > last:
                    last = curr.val
                else:
                    return False
            
            # 這裡不用先檢查curr.right和stack.append()，前面的if curr會做這件事
            curr = curr.right

        return True