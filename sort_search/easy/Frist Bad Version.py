# First Bad Version
# You are a product manager and currently leading a team to develop a new product. Unfortunately, the latest version of your product fails the quality check. Since each version is developed based on the previous version, all the versions after a bad version are also bad.
# Suppose you have n versions [1, 2, ..., n] and you want to find out the first bad one, which causes all the following ones to be bad.

# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

# 資料有排序，可用binary search
# 注意version從1到n
# 注意找到的bad version不一定是第一個，需要再檢查上一個是否為bad version

# 暴力解，當n很大時可能會遇到memory error，時間複雜度O(n)
class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        for ver in range(1, n+1):
            if isBadVersion(ver):
                return ver
            
# Binary Search，時間複雜度O(logn)
class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        left = 1  # 注意從1開始
        right = n

        while left <= right:
            mid = (left+right)//2

            if not isBadVersion(mid):  # bad version在後面，更新下界
                left = mid + 1
            else:
                if not isBadVersion(mid-1):  # 確認是第一個bad version
                    return mid
                right = mid -1  # bad version在前面，更新上界
        
        return None  # 若找不到bad version