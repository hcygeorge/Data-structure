# 若為alternating bits，位元右移一位後做XOR會得到全1
# 如何確認XOR後是否全為1?
# 若全為1，則加1後應該會進位，再與加1前做AND後必會=0

class Solution(object):
    def hasAlternatingBits(self, n):
        """
        :type n: int
        :rtype: bool
        """
        n = n ^ (n >> 1)
        return n & (n+1) == 0