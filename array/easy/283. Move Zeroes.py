# Given an integer array nums, 
# move all 0's to the end of it while maintaining the relative order of the non-zero elements.

# tipss:
# 題目要求inplace
# 左右指針可以將0排到最後面，但是無法讓非0維持原本順序
# 快慢指針負責指著最後一個0值等著與後面交換
# blind point: 會猶豫s在開頭非0時怎麼處理，其實非0時s,l會在同一個位置，交換等於沒換
# attempt count: 3
# O(n), O(1)

# frist try
class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        fast = 0
        slow = 0

        while fast < len(nums):
            if nums[fast] == 0:
                fast += 1
                # 遇到0時，slow停著等著與後面的非0值交換
            else:
                if fast != slow:  # 這是多餘的檢查，因為即使一樣交換也不影響結果
                    nums[fast], nums[slow] = nums[slow], nums[fast]
                fast += 1
                slow += 1  # 交換完畢，可以指向下一個值

# second try
class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        
        p1 = 0
        p2 = 0  # 負責指著最後一個經過的0，等到p1走道非0後交換

        while p1 < len(nums):
            if nums[p1] == 0:
                p1 += 1
            else:
                nums[p1], nums[p2] = nums[p2], nums[p1]
                p1 += 1
                p2 += 1
                
# third try
class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        # create 2 pointers
        f = 0
        s = 0  # point to the last zero during traverse

        # traverse the arrays
        while f < len(nums):
            if nums[f] == 0:
                f += 1
            elif nums[f] != 0:
                nums[f], nums[s] = nums[s], nums[f]
                f += 1
                s += 1
        
        return nums