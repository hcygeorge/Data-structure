# tips: 分別用兩個指針連結奇偶串列，while條件是兩個指針的next都存在
# 注意如果選擇先處理偶數串列再處理奇數串列會出錯，因為原本的head連結已被前者改變
# 因此只能在同時處理奇偶串列再合併兩個串列

class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return None
        if not head.next:
            return head
        
        p = head
        q = head.next
        even_head = p
        odd_head = q
        
        while p.next and q.next:
            p.next = p.next.next
            q.next = q.next.next
            
            p = p.next
            q = q.next
            
        p.next = odd_head

        return even_head

            