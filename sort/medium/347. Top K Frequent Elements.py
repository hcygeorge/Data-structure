import random
class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        # create pivot
        k = len(nums) - k
        def select(nums, k):
            pivot = random.randint(0, len(nums) - 1)

            # collenct partition
            l = []
            r = []

            # sort
            for i, n in enumerate(nums):
                if n <= nums[pivot] and i != pivot:
                    l.append(n)
                if n > nums[pivot]:  # 用else會導致pivot被加入r
                    r.append(n)

            # compare idx and pivot_idx
            if len(l) == k:
                return nums[pivot]
            elif len(l) < k:
                return select(r, k - (len(l) + 1))  # 新位置是扣掉前面的數量
            else:
                return select(l, k)

        return select(nums, k)