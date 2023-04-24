# Valid Mountain Array
# https://leetcode.com/problems/valid-mountain-array/description/
# edge case: arr長度不夠、peak是第一個元素或最後一個
# 我的做法是在迭代過程中檢查元素是否比前一個更大，找到peak後改變檢查條件
# 官方解答將迭代過程分成找到peak前與找到peak後，這樣寫程式碼看起來更簡練

class Solution(object):
    """
    First try
    用peak用控制迭代時的檢查條件，在peak之前要遞增，之後則遞減。
    """
    def validMountainArray(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        peak = False
        
        # edge case 1: array too short
        if len(arr) < 3:
            return False
        
        
        for idx in range(len(arr)):
            if idx == 0:
                if arr[0] < arr[1]:
                    continue
                else:  # edge case 3: peak is the first element
                    return False
            
            if not peak:
                if arr[idx] > arr[idx-1]:
                    continue
                elif arr[idx] == arr[idx-1]:
                    return False
                else:
                    peak = True
                    continue
            else:
                if arr[idx] < arr[idx-1]:
                    continue
                else:
                    return False
        
        if peak:
            return True
        else:  # edge case 2: peak is the last element
            return False

# 官方解
class Solution(object):
    """
    Official solution
    """
    def validMountainArray(self, A):
        N = len(A)
        i = 0

        # walk up
        while i+1 < N and A[i] < A[i+1]:
            i += 1

        # peak can't be first or last
        if i == 0 or i == N-1:
            return False

        # walk down
        while i+1 < N and A[i] > A[i+1]:
            i += 1

        return i == N-1
    
# 第二次解答
class Solution(object):
    """
    Second try
    將迭代分成上升和下降兩部分，但未將peak在開頭或結尾的edge case單獨出來。
    """
    def validMountainArray(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        length = len(arr)

        # edge case
        if length < 3:
            return False

        # climb up and find peak
        for i in range(1, length):
            if arr[i] > arr[i-1]:
                continue
            elif arr[i] == arr[i-1]:
                return False
            else:
                if i == 1:
                    return False
                break

        # go down
        for j in range(i, length):
            if arr[j] < arr[j-1]:
                continue
            else:
                return False
        
        return True

# 第三次解，加入edge case判斷
class Solution(object):
    def validMountainArray(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        len_arr = len(arr)
        if len_arr < 3:
            return False

        peak = None
        pre = arr[0]
        # climb up and find peak
        for i in range(1, len_arr):
            if arr[i] > pre:
                pre = arr[i]
            elif arr[i] == pre:
                return False
            else:
                peak = arr[i-1]
                break

        # edge case: head is peak or tail is peak 
        if peak == arr[0] or peak == None:
            return False

        # go down
        for j in range(i, len_arr):
            if arr[j] < pre:
                pre = arr[j]
            else:
                return False

        return True