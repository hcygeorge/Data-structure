# You are given two integer arrays nums1 and nums2, 
# sorted in non-decreasing order, and two integers m and n, 
# representing the number of elements in nums1 and nums2 respectively.
# Merge nums1 and nums2 into a single array sorted in non-decreasing order.
# The final sorted array should not be returned by the function, 
# but instead be stored inside the array nums1. To accommodate this, nums1 has a length of m + n, 
# where the first m elements denote the elements that should be merged, 
# and the last n elements are set to 0 and should be ignored. nums2 has a length of n.

# attempt count: 1

# tips:
# 應該從右邊開始走訪nums1
# 需要3個指針
# 注意nums2可能有剩下的元素(因為比較小所以沒有插入nums1)

# blind spot:
# 記得先檢查nums1, nums2存在性
# 從左邊開始遍歷需要額外空間暫存較大的元素，無法處理nums2連續幾個元素都小於nums1[p1]的情況，交換後無法維持遞增狀態
# 注意nums2可能有剩下的元素(因為比較小所以沒有插入nums1)，而nums1剩下因為已經遞增排序，無需處理

# first try(wrong)
# 從左邊開始遍歷需要額外空間暫存較大的元素，失敗
class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        if not nums1 or not nums2:
            return None
        
        # create pointers
        p1, p2 = 0, 0
        
        # traverse through nums1
        while p1 < len(nums1):
            if nums1[p1] > nums2[p2] or nums1[p1] == 0:
                nums1[p1], nums2[p2] = nums2[p2], nums1[p1]
                
                if nums2[p2] == 0:
                    p2 += 1

            p1 += 1

# first try
class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        if not nums1 or not nums2:
            return None
        
        p, p1, p2 = m+n-1, m-1, n-1
        
        while p1 >= 0 and p2 >= 0:
            if nums1[p1] > nums2[p2]:
                nums1[p] = nums1[p1]
                p1 -= 1
            else:
                nums1[p] = nums2[p2]
                p2 -= 1
            p -= 1
            
        # attach the rest of nums2 to the left of nums1
        if p2 >= 0:
            nums1[:p+1] = nums2[:p2+1]