# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# tips:用快慢指針，快指針先走n步，慢指針再開始一起走，當快指針走完，慢指針剛好在倒數n個node的前一個


# first try: 用額外的空間儲存node，不是最好的做法
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        # 收集每個node
        p = head
        counter = []
        while p:
            counter.append(p)
            p = p.next
        
        l = len(counter)

        # 刪除第一個節點
        if n == l:
            head = head.next
        # 刪除最後一個節點
        elif n == 1:
            counter[l-2].next = None
        # 刪除中間節點
        else:
            counter[l-n-1].next = counter[l-n+1]
        
        return head
        
# first try: 快指針先走n步慢指針再一起走，不用額外空間
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        fast = head
        for _ in range(n):
            fast = fast.next
        
        # 如果此時 fast 為空，表示要刪除的是頭節點
        if fast == None:
            return head.next
        
        slow = head
        while fast.next:
            fast = fast.next
            slow = slow.next
            
        slow.next = slow.next.next
        
        return head