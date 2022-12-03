# Replace Elements with Greatest Element on Right Side
# hint1 loop data from the end
# hint2 keep max value
# hint3 keep elements in temp before replace it with max value
class Solution(object):
    def replaceElements(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        l = len(arr)
        idx = l - 1
        max_num = arr[idx]
        while idx >= 0:
            if idx == l - 1:
                arr[idx] = -1
            else:
                temp = arr[idx]
                arr[idx] = max_num
                if temp > max_num:
                    max_num = temp
            idx -= 1
            
        return arr
    
    
