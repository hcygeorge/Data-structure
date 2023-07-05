# tips: 先計算元素出現次數，再以出現次數作為桶子編號，將出現x次的元素放到編號x的桶子
# 由於題目有唯一解，我們只要依序把最大編號的桶子數字取出，直到得到k個元素為止。
# 時間複雜度O(N+k)，k是前k大元素個數
# 這題也能用headq(max heap)解

class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        
        freq_map = {}
        for d in nums:
            freq_map[d] = freq_map.get(d, 0) + 1
        
        bucket = [[] for _ in range(max(freq_map.values()) + 1)]
        
        for d, freq in freq_map.items():
            bucket[freq].append(d)
        
        res = []
        for b in range(len(bucket)-1, 0, -1):
            res += bucket[b]
            if len(res) >= k:
                return res