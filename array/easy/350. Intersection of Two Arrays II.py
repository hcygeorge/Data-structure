# Given two integer arrays nums1 and nums2,
# return an array of their intersection.
# Each element in the result must appear as many times as it shows in both arrays
# and you may return the result in any order.

# tips:
# 只用dict計算nums1出現次數，走訪nums2時一邊扣掉次數一邊將元素加入result

# blined spot:
# 扣掉次數一邊將元素加入result可以在走訪nums2時一起做，不需要分開處理


# 建立hash map後，找出共同的元素並取最小值，O(n)
# 注意min, max原本複雜度是O(n)，但這邊只固定比較2個資料大小，所以複雜度為O(1)
class Solution:
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        
        def create_dict(nums):
            mapping = {}
            for x in nums:
                if x in mapping:
                    mapping[x] += 1
                else:
                    mapping[x] = 1
            return mapping
        
        nums1_dict = create_dict(nums1)
        nums2_dict = create_dict(nums2)
        
        res = []
        for key in nums1_dict.keys():
            if key in nums2_dict:
                freq = min(nums1_dict[key], nums2_dict[key])
                res += [key] * freq
                
        return res
    

# 只算nums1的資料出現次數，接著檢查nums2是否出現在hash map中，有的話資料為交集，hash map次數要減1
class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        inter = []

        dict01 = {}
        for i in nums1:
            if dict01.get(i):
                dict01[i] += 1
            else:
                dict01[i] = 1
        
        for i in nums2:
            if dict01.get(i) and dict01[i] > 0:
                dict01[i] -= 1
                inter.append(i)

        return inter

    
# 先排序後可用2 pointers解題
# 用try except處理index out of range的問題(代表其中一個arr已經檢查完畢)
# 因為有用到排序，所以複雜度為O(nlogn)
class Solution2:
    def intersect(self, nums1, nums2):
        
        nums1 = sorted(nums1)
        nums2 = sorted(nums2)
        res = []
        p1, p2 = 0, 0
        
        while True:
            try:
                if nums1[p1] == nums2[p2]:
                    res.append(nums1[p1])
                    p1 += 1
                    p2 += 1
                elif nums1[p1] > nums2[p2]:
                    p2 += 1
                else:
                    p1 += 1
            except IndexError:
                break
        
        return res
    

# second try
class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        counter = {}
        for i in nums1:
            counter[i] = counter.get(i, 0) + 1

        for j in nums2:
            counter[j] = counter.get(j, 0) - 1

        inter = []
        for i in nums1:
            if counter[i] <= 0:
                inter.append(i)
            elif counter[i] > 0:
                counter[i] -= 1
        
        return inter