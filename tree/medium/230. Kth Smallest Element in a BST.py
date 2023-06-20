
# recursion: use inorder traversal to collect sorted values
class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        res = []
        
        def traverse(node):
            if not node:
                return None

            traverse(node.left)
            res.append(node.val)
            traverse(node.right)        
        
        traverse(root)
        return res[k-1]

# iteration: use k as counter to return kth-smallest value 
class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        res = []
        stack = []
        curr = root
        
        while curr or stack:
            if curr:
                stack.append(curr)
                curr = curr.left
            else:
                curr = stack.pop()
                k -= 1
                if k == 0:
                    return curr.val
                curr = curr.right