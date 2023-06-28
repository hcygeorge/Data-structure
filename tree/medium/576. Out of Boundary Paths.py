# tips: 用dfs遞迴的探討在座標i, j且剩下N步時，還有幾種路徑可走出界
# 每次都可檢查往上下左右走是否出界，若是則走法累加1，否則要繼續累加N-1的走法
# dic用於紀錄已知的(i, j, N)有幾種走法，減少重複計算
class Solution(object):
    def findPaths(self, m, n, maxMove, startRow, startColumn):
        """
        :type m: int
        :type n: int
        :type maxMove: int
        :type startRow: int
        :type startColumn: int
        :rtype: int
        """

        def dfs(i, j, N, dic):
            if (i, j, N) in dic:
                return dic[(i, j, N)]
            if N == 0:
                return 0

            r = 0
            if i-1 < 0:
                r += 1
            else:
                r += dfs(i-1, j, N-1, dic)
            if j-1 < 0:
                r += 1
            else:
                r += dfs(i, j-1, N-1, dic)
            if i+1 == m:
                r += 1
            else:
                r += dfs(i+1, j, N-1, dic)
            if j+1 == n:
                r += 1
            else:
                r += dfs(i, j+1, N-1, dic)
        

            dic[(i, j, N)] = r
            return r

        return dfs(startRow, startColumn, maxMove, {}) % (10**9 + 7)
