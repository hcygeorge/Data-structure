# Given an integer array nums and an integer k, return the kth largest element in the array.
# Note that it is the kth largest element in the sorted order, not the kth distinct element.
# You must solve it in O(n) time complexity.
# 使用quick select方法，利用quick sort的partition概念將數列切成子數列
# 其中一個收集小於pivot的數字，另一個則收集大的
# 然後比較pivot位置和k-th的位置，判斷kth在哪個子數列內
# 之後遞迴在子數列中繼續找kth
# 與quick sort一樣，平均時間複雜度O(n)，最糟O(n^2)
# 因為不用排序所有數字，所以實務上會比完整排序完再找kth快

import random
class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        k = len(nums) - k  # 找第k大 == 第N-k+1小，index == N-k
        def select(nums, k):
            # create pivot
            pivot = random.randint(0, len(nums) - 1)

            # create partition
            l = []
            r = []

            # sort
            for i, n in enumerate(nums):
                if n <= nums[pivot] and i != pivot:  # pivot不能被加進去
                    l.append(n)
                if n > nums[pivot]:  # 用else會導致pivot被加入r
                    r.append(n)

            # find the partition with k
            if len(l) == k:
                return nums[pivot]
            elif len(l) > k:
                return select(l, k)
            else:
                return select(r, k - (len(l) + 1))  # 扣掉前面陣列得到新索引

        return select(nums, k)

