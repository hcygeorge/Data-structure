# tips: 先計算元素出現次數，再以出現次數作為桶子編號，將出現x次的元素放到編號x的桶子
# 由於題目有唯一解，我們只要依序把最大編號的桶子數字取出，直到得到k個元素為止。
# 時間複雜度O(N+k)，k是前k大元素個數
# 這題也能用headq(max heap)解

class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        l = 0
        r = len(nums) - 1
        p = 0

        while p <= r:
            if nums[p] == 2:
                nums[p], nums[r] = nums[r], nums[p]
                r -= 1
            elif nums[p] == 0:
                nums[p], nums[l] = nums[l], nums[p]
                l += 1
                p += 1
            else:
                p += 1

class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        freq_map = {}

        for d in nums:
            freq_map[d] = freq_map.get(d, 0) + 1

        bucket = [[] for _ in range(max(freq_map.values()) + 1)]

        for k, v in freq_map.items():
            bucket[v].append(k)

        res = []
        for b in range(len(bucket)-1, 0, -1):
            res += bucket[b]
            if len(res) >= k:
                return res[k]