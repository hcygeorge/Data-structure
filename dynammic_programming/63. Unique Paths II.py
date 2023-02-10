# 提示: 遇到障礙時，方法樹為0
# 在邊界時，抵達方法只剩一邊
# 起點有障礙就直接結束
class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        if obstacleGrid[0][0] == 1:
            return 0

        row, col = len(obstacleGrid), len(obstacleGrid[0])
        dp = [[0 for j in range(col)] for i in range(row)]
        dp[0][0] = 1
        
        for i in range(row):
            for j in range(col):
                if obstacleGrid[i][j] == 1:
                    dp[i][j] = 0
                else:
                    if i-1 >= 0:
                        dp[i][j] += dp[i-1][j]
                    if j-1 >= 0:
                        dp[i][j] += dp[i][j-1]

        return dp[-1][-1]
