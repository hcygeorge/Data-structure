# Valid Mountain Array
# edge case: arr長度不夠、peak是第一個元素或最後一個
# 我的做法是在迭代過程中檢查元素是否比前一個更大，找到peak後改變檢查條件
# 官方解答將迭代過程分成找到peak前與找到peak後，這樣寫程式碼看起來更簡練

# 我的解法
class Solution(object):
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