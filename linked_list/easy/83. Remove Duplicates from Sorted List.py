# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# 錯誤1:curr應指向當下而非下一個node
# pre = head
# curr = head.next
# 錯誤2:檢查post忘了考慮post存在與否

# 建立變數curr指向當下的node
# 變數post指向下一個node
# 持續檢查post是否存在且值和curr相同
# 直到節點不存在或值不相同，將post接在curr後面(等於跳過中間重複的值)
# 接著curr移動到下個值curr.next開始繼續檢查
# 檢查完畢後回傳head
# O(n);O(1)

# 犯錯
# 1: 沒有用curr指向當下的node
# 2: 沒有用第二層while檢查post
# 3: post.val == curr.val應作為while的條件，否則while post會遍歷所有node
# 4: post = curr.next放在while curr之前

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        curr = head
        while curr:
            post = curr.next
            while post and post.val == curr.val:
                post = post.next

            curr.next = post
            curr = curr.next

        return head
    
# 邏輯與前次一樣，一個指針指著最後一個node，另一個指針往後找下一個不重複的node
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return head

        last = head
        curr = head.next

        while curr:
            if curr.val != last.val:
                last.next = curr
                last = curr

            curr = curr.next

        last.next = None
        return head


