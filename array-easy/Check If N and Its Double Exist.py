class Solution(object):
    def checkIfExist(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        checked = set()  #  set is implemented as a hash table
        length = len(arr)
        
        for idx in range(length):
            if (arr[idx] * 2 in checked) or (float(arr[idx]) / 2 in checked):
                return True
            else:
                checked.add(arr[idx])
                
        return False