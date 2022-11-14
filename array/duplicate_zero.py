# 1. 計算0的個數，新array的最後一個0不用複製
# 2. 計算新array的長度
# 3. 從array尾部往回遍歷，若為0則複製兩次放在結尾，若非0則複製一次
# https://leetcode.com/problems/duplicate-zeros/solutions/393433/official-solution/

class Solution(object):
    def duplicateZeros(self, arr):
        """
        :type arr: List[int]
        :rtype: None Do not return anything, modify arr in-place instead.
        """
        length = len(arr) - 1
        num_zero = 0

        # Count 0 to be duplicated
        for left in range(length + 1):
            # when to stop looping
            if left > length - num_zero:
                break
                
            # count the 0s
            if arr[left] == 0:
                # edge case: the last 0 doesn't need to be duplicated
                if left == length - num_zero:
                    arr[length] = 0 # For this zero we just copy it without duplication.
                    length -= 1
                    break
                    
                num_zero += 1
                
        # Get the length of final array
        new_length = length - num_zero
        
        # Copy zero twice, and non zero once.
        for i in range(new_length, -1, -1):
            if arr[i] == 0:
                arr[i + num_zero] = 0
                num_zero -= 1
                arr[i + num_zero] = 0
            else:
                arr[i + num_zero] = arr[i]