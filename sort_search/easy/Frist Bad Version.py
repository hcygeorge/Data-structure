# First Bad Version
# You are a product manager and currently leading a team to develop a new product. Unfortunately, the latest version of your product fails the quality check. Since each version is developed based on the previous version, all the versions after a bad version are also bad.
# Suppose you have n versions [1, 2, ..., n] and you want to find out the first bad one, which causes all the following ones to be bad.

# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

# 資料有排序，可用binary search
# 注意version從1到n
# 注意找到的bad version不一定第一個，需要再檢查上一個是否為bad version
# O(logn)
class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        low = 1
        up = n
        
        while low <= up:
            mid = (low + up) // 2
            if not isBadVersion(mid):
                low = mid + 1
            else:
                if mid == 1 or not isBadVersion(mid-1):
                    return mid
                else:
                    up = mid - 1
        
        return None  # 理論上不會不存在bad version