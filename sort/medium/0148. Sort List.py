# 切分: 利用快慢指針，fast走兩步slow走一步，當fast走到底，slow的剛好是後半段的head
# 還需要建立一個prev記住前一個slow，用prev.next = None切開兩個list
# 合併: 建立dummy head，連接head和slow兩個list

# 犯錯: 忘記先檢查list長度，導致maximum recursion

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head

        fast, slow = head, head
        prev = slow

        while fast and fast.next:
            fast, prev, slow = fast.next.next, slow, slow.next

        prev.next = None

        return self.merge(self.sortList(head), self.sortList(slow))

    def merge(self, l, r):
        dummy = ListNode()
        p = dummy
        while l and r:
            if l.val < r.val:
                p.next = l
                l = l.next
            else:
                p.next = r
                r = r.next
            p = p.next

        p.next = l or r

        return dummy.next