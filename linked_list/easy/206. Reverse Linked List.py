# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# tips:
# 用current指向當下的node，prev指向前個node
# 每次迭代先用next_node暫存下個節點，將current連接到prev，然後current和prev在往下移動
# 記得回傳prev

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        prev = None  # 記住前一個node
        current = head
        
        while current:
            next_node = current.next  # 暫存下個node
            current.next = prev  # 連接上個node
            prev = current
            current = next_node
            
        return prev  # 走完head會變成尾，current會變成None，要回傳prev