# try:2
# Merge Two Sorted Lists
# https://leetcode.com/problems/merge-two-sorted-lists/description/
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# 提示
# 1. 建立新的head = ListNode儲存merged list
# 2. 用prev指向最後一個節點
# 3. 迭代條件是list1 list2兩個都要有節點
# 4. prev.next接上還有剩節點的list
# 5. 記得head的下一個才是真的起點

# 先建立一個空的head作為merged list的head
# 建立prev負責連接node
# 假設list1, list2都是升冪排序，從最前面開始比較大小
# 小的藉由prev連接在merged list後面
# 每次連接後記得切換到最後一個node
# 比較大小直到其中一個list空了，則剩下的node可以整串接到merged list後面
# 記得一開始建立的head是空的，因此下個node才是真正的head

# 犯錯1: 沒有用curr指向當下的node
# 犯錯2: curr連接後沒有移動到下個node
# 犯錯3: 沒有把剩下的list連接在curr後面

class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        merged = ListNode(None)  # head node of output
        p = merged  # use p to connect nodes
        
        # loop until one of the list is empty
        while list1 and list2:
            if list1.val <= list2.val:  # equal sign affects when list1 == list2
                p.next = list1
                list1 = list1.next
            else:
                p.next = list2
                list2 = list2.next
            p = p.next  # don't forget to point to next node!
                
        # the rest of the nodes in one of the list can be attatched behind
        p.next = list1 or list2 
        
        # remind that head is None, the next node is the real head
        return merged.next