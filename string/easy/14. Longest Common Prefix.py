# Write a function to find the longest common prefix string amongst an array of strings.

# If there is no common prefix, return an empty string "".

# tips:
# 用一個指針p走訪list，再用兩個指針p1, p2走訪prefix和當下的字串，用於比對prefix
# 如果p1, p2其中一個先走完，則代表新prefix會停在先走完的指針

class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        
        prefix = strs[0]
        p = 1
        
        while p < len(strs):
            p1, p2 = 0, 0
            while p1 < len(prefix) and p2 < len(strs[p]):
                if prefix[p1] == strs[p][p2]:
                    p1 += 1
                    p2 += 1
                else:
                    break
            
            prefix = prefix[:min(p1, p2)]
                    
            p += 1
            
        return prefix
            