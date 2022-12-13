# Merge Two Sorted Lists
# https://leetcode.com/problems/merge-two-sorted-lists/description/
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# 先建立一個空的head作為merged list的head
# 建立prev負責連接node
# 假設list1, list2都是升冪排序，從最前面開始比較大小
# 小的藉由prev連接在merged list後面
# 每次連接後記得切換到最後一個node
# 比較大小直到其中一個list空了，則剩下的node可以整串接到merged list後面
# 記得一開始建立的head是空的，因此下個node才是真正的head

class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        head = ListNode(None)  # head node of output
        prev = head  # use prev to connect nodes
        
        # loop until one of the list is empty
        while list1 and list2:
            if list1.val <= list2.val:  # equal sign affects when list1 == list2
                prev.next = list1
                list1 = list1.next
            else:
                prev.next = list2
                list2 = list2.next
            prev = prev.next  # don't forget to point to next node!
                
        # the rest of the nodes in one of the list can be attatched behind
        prev.next = list1 or list2 
        
        # remind that head is None, the next node is the real head
        return head.next