# tips: 檢查每個節點，若左子樹存在則連接右子樹，若右存在則連接root.next的左子樹
# 迭代時先建立指標leftest走訪每一層最左邊的節點，因為是完美二元樹所以一定可以走到最底層
# 再建立指標curr從每個leftest走訪該層的節點並按照上述邏輯連接

# recursion
class Solution(object):
    def connect(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        if not root:
            return None
        
        if root.left:
            root.left.next = root.right
        
        if root.right and root.next:
            root.right.next = root.next.left
                
        self.connect(root.left)
        self.connect(root.right)
        
        
        return root

# iteration
class Solution(object):
    def connect(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        if not root:
            return None
        
        leftest = root
        
        while leftest:
            curr = leftest
            while curr:
                if curr.left:
                    curr.left.next = curr.right
                if curr.right and curr.next:
                    curr.right.next = curr.next.left
                
                curr = curr.next
                
            leftest = leftest.left
        
        return root