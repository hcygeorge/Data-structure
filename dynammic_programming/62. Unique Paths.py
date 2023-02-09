# 提示: 走到i,j的方法數=走到i,j-1的方法+走到i-1,j的方法
# 用階乘解(m+n-2)!/(m-1)!(n-1)!，當m,n很大時容易overflow
class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """

        dp = [[0 for j in range(n)] for i in range(m)]
        # don't use df = [[0]*n]*m, they will point to same memory position

        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    dp[i][j] = 1
                elif i == 0 and j > 0:
                    dp[i][j] = dp[i][j-1]
                elif i > 0 and j == 0:
                    dp[i][j] = dp[i-1][j]
                else:
                    dp[i][j] = dp[i-1][j] + dp[i][j-1]
        return dp[-1][-1]
