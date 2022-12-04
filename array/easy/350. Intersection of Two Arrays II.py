# Given two integer arrays nums1 and nums2,
# return an array of their intersection.
# Each element in the result must appear as many times as it shows in both arrays
# and you may return the result in any order.

# Hash map統計出現次數，再比對出交集的資料，以出現次數最少的為主
# O(n)
# 注意min, max原本複雜度是O(n)，但這邊只固定比較2個資料大小，所以複雜度為O(1)
# 其實可以只算nums1的資料出現次數，接著檢查nums2是否出現在hash map中，有的話資料為交集，hash map次數要減1
class Solution1:
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