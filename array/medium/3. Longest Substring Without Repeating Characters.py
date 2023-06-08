

# brute-force solution, O(n^2)
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        last_str = ''
        p = 0
        while p < len(s):
            temp_str = s[p]
            
            q = p + 1
            while q < len(s):
                if s[q] in temp_str:
                    break
                else:
                    temp_str += s[q]
                    q += 1
                    
            if len(temp_str) > len(last_str):
                last_str = temp_str

            p += 1
        
        return len(last_str)
        