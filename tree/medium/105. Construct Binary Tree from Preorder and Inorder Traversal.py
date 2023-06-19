# tips: preorder每個值都是根與左子樹的根和右子樹的根，可用於分割inorder
# 分割後的inorder長度可以反過來分割preorder，將分割的inorder和preorder代入uildTree函數，遞迴的建立整棵樹

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        if not preorder or not inorder:
            return None
        
        # get index of inorder from preorder
        root_val = preorder[0]
        node = TreeNode(val=root_val)
        idx = inorder.index(root_val)
        
        # split inorder
        left_inorder = inorder[:idx]
        right_inorder = inorder[idx+1:]
    
        # split preorder
        left_preorder = preorder[1:1+len(left_inorder)]
        right_preorder = preorder[1+len(left_inorder):]  # note that it is left_inorder
        
        # recursion
        node.left = self.buildTree(left_preorder, left_inorder)  
        node.right = self.buildTree(right_preorder, right_inorder)
        
        return node
        
    