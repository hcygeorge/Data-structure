# Wrong solution
# 可能遇到刪掉左邊(右邊)字元後只有下一對字元相同，
# 而刪掉右邊(左邊)後面的字串才全都相同的情況
# 如cupuu, upucu應該刪掉右邊的u
# ecec, acec應該刪掉左邊的e
class Solution(object):
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        left = 0
        right = len(s) - 1
        deleted = False

        while left <= right:
            print(left, right, s[left], s[right])
            if s[left] == s[right]:
                left += 1
                right -= 1
            elif s[left] == s[right-1] and not deleted:
                left += 1
                right -= 2
                deleted = True
            elif s[left+1] == s[right] and not deleted:
                    left += 2
                    right -= 1
                    deleted = True
            else:
                return False
        
        return True
    
# 從刪除字後重新開始檢查回文，全部都對才回傳True
class Solution(object):
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        def check(s, l, r):
            while l <= r:
                if s[l] == s[r]:
                    l += 1
                    r -= 1
                else:
                    return False
            return True

        left = 0
        right = len(s) - 1

        while left <= right:
            print(left, right, s[left], s[right])
            if s[left] == s[right]:
                left += 1
                right -= 1
            else:
                return check(s, left+1, right) or check(s, left, right-1)       
        return True