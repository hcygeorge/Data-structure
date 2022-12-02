# Given two strings s and t, return true if t is an anagram of s, and false otherwise.

# Hash Map
# O(n), O(n)
# 統計s的字出現次數，然後扣掉t的字出現次數，若次數全為0則代表為anagram
# 事先檢查s和t長度和字出現次數在扣除前已經是0，就不用檢查是否次數是否全為0
# 補充: 實際工作時可用Counter處理此問題
class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        len_s = len(s)
        len_t = len(t)
        if len_s != len_t:
            return False
        count = {}
        for idx in range(len_s):
            if s[idx] in count:
                count[s[idx]] += 1
            else:
                count[s[idx]] = 1
                
        for idx in range(len_t):
            if t[idx] not in count or count(t[idx]) == 0:
                return False
            else:
                count[t[idx]] -= 1
                
        # for k, v in count.items():
        #     if v != 0:
        #         return False
        
        return True