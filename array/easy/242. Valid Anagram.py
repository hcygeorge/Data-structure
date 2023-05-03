# Given two strings s and t, return true if t is an anagram of s, and false otherwise.
# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase,
# typically using all the original letters exactly once.

# tips: 
# 統計s的字出現次數，然後扣掉t的字出現次數，若次數全為0則代表為anagram
# 事先檢查s和t長度和字出現次數在扣除前已經是0，就不用檢查是否次數是否全為0
# 補充: 實際工作時可用Counter處理此問題

# blind spot:
# 記得先檢查字串長度是否一致

# first try: hash table解
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
                
        for k, v in count.items():
            if v != 0:
                return False
        
        return True
    
# second try: hash table解，程式碼有比較簡練
class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False
        
        count = {}
        
        for char in s:
            count[char] = count.get(char, 0) + 1
            
        for char in t:
            if count.get(char):
                count[char] -= 1
            else:
                return False
                
        for val in count.values():
            if val != 0:
                return False
            
        return True

# second try: 排序解，複雜度較高
class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False
        return sorted(s) == sorted(t)