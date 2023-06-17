# tips: 可以在加總前先檢查個別ListNode是否存在，或是分兩步處理兩個都存在和只剩一個存在的情況
# 記得最後還有檢查是否進位
# attempt count: 1

# first try
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        
        dummy = ListNode()
        p = dummy
        carry = 0
        while l1 and l2:
            sum_val = l1.val + l2.val + carry
            if sum_val >= 10:
                sum_val -= 10
                carry = 1
            else:
                carry = 0
                
            p.next = ListNode(val=sum_val)
            p = p.next
            l1 = l1.next
            l2 = l2.next
        
        rest = l1 or l2
        while rest:
            sum_val = rest.val + carry
            if sum_val >= 10:
                sum_val -= 10
                carry = 1
            else:
                carry = 0
                
            p.next = ListNode(val=sum_val)
            p = p.next
            rest = rest.next
        
        if carry == 1:
            p.next = ListNode(val=1)
        
        return dummy.next
            
        