# Given two strings needle and haystack,
# return the index of the first occurrence of needle in haystack,
# or -1 if needle is not part of haystack.


# tips: 用兩個指針走訪字串比對，當走訪完needle代表needle是haystack的子字串
# 當比對失敗時needle的指針要歸零
# 有些案例中needle可能與前面部分正確的字串有重疊情況，因此比對失敗時haystack指針要回到上一次比對成功的位置
# 有點難解釋，用範例說明:"mississippi"中"issip"和前面issis重疊，
# 所以走到missis發現比對失敗，要回到mis開始檢查

class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        p1, p2 = 0, 0
        
        while p1 < len(haystack) and p2 < len(needle):
            print(p1, p2)
            if haystack[p1] == needle[p2]:
                p2 += 1
            else:
                p1 -= p2  # back to the first matched char
                p2 = 0
            
            p1 += 1
        
        if p2 == len(needle):
            return p1 - len(needle)
        else:
            return -1
        