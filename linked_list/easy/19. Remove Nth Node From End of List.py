# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# tips:
# 走過list，收集節點和計算節點個數
# 根據節點的位置決定怎麼跳過節點

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
        
        