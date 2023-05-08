# Write a function to find the longest common prefix string amongst an array of strings.

# If there is no common prefix, return an empty string "".

# tips:
# 用一個指針p0走訪list，再用指針p1走訪prefix和當下的字串，用於比對prefix
# 如果p1其中一個先走完，則代表新的prefix會停在指針走到的位置，利用p1截斷prefix

class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        prefix = strs[0]
        p0 = 1
        while p0 < len(strs):
            if strs[p0] == '':
                return ''
            p1 = 0
            while p1 < len(prefix) and p1 < len(strs[p0]):
                if prefix[p1] == strs[p0][p1]:
                    p1 += 1
                else:
                    break
            prefix = prefix[:p1]
            p0 += 1
            
        return prefix