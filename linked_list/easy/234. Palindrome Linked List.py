# Given the head of a singly linked list, return true if it is a palindrome, or false otherwise.
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# tips:
# 用快慢指針找到中間節點，接著反轉後半段節點，然後比對前半段和反轉後半段的節點值，無須額外空間


# first try: 先反轉鏈結順序，順便收集值，再比較值是否相等，需要額外空間
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        current = head
        prev = None
        vals = []
        while current:
            vals.append(current.val)
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
            
        for v in vals:
            if prev.val == v:
                prev = prev.next
            else:
                return False
            
        return True

# first try: 用快慢指針找到中間節點，接著反轉後半段節點，然後比對前半段和反轉後半段的節點值，無須額外空間
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        # only one node case
        if head.next == None:
            return True

        # find middle node
        slow, fast = head, head
        while fast:
            fast = fast.next.next
            slow = slow.next
        if fast:
            slow = slow.next

        # reverse second half
        prev = None
        curr = slow
        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
        
        # compare value
        while prev:
            if head.val == prev.val:
                head = head.next
                prev = prev.next
            else:
                return False

        return True
            
        