# Given head, the head of a linked list, determine if the linked list has a cycle in it.
# There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer.
# Internally, pos is used to denote the index of the node that tail's next pointer is connected to. Note that pos is not passed as a parameter.
# Return true if there is a cycle in the linked list. Otherwise, return false.


# tips:
# 用快慢指針，快指針從head.next開始一次走兩步，慢指針從head開始一次走一步，若鏈結有循環則快指針會追上慢指針
# 注意循環的節點位置不一定在頭，因此慢指針不能停著等快指針追上

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# first try
class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head or not head.next:
            return False
        
        slow, fast = head, head.next
        
        while slow != fast:
            if not fast or not fast.next:
                return False
            
            slow = slow.next
            fast = fast.next.next

        return True