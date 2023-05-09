# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        # 將現在的node取代下個node，沒有變數指向下個node指向的物件，GC會自動回收該物件
        node.val = node.next.val
        node.next = node.next.next
        
class Solution(object):
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        # 主動刪除下個node指向的物件
        nextnode = node.next
        node.val = nextnode.val
        node.next = nextnode.next

        del nextnode