# 用字典儲存每個字出現次數
# 再根據出現次數計算回文長度
# 所有成對的(//2 == 0)都能加進回文，回文長度+2
# 單獨的字只能放回文中間，而且僅限一次，回文長度+1

class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        l = 0
        counter = {}

        # count number of char
        for char in s:
            counter[char] = counter.get(char, 0) + 1

        # accumulate length of palindrome
        for k, v in counter.items():
            l += (v // 2) * 2
            # 利用l % 2 == 0判斷回文是否還沒有加上中間字
            if l % 2 == 0 and v % 2 == 1:
                l += 1 

        return l
        