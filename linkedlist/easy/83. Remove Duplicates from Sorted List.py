# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# 建立迭代器ite用於檢查linked list
# 當下個節點(temp)存在且值和前者相同，則繼續檢查
# 直到節點不存在或值不相同，ite.next指向該節點(等於跳過中間相同的值)
# 接著從下個值(ite.next)開始繼續檢查
# 檢查完畢後回傳head
# O(n);O(1)
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        ite = head
        while ite:
            temp = ite.next
            while temp and temp.val == ite.val:
                temp = temp.next
            ite.next = temp
            ite = ite.next
        
        return head
