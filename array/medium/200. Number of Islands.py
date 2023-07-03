# 利用dfs走訪每個1且尚未走過的座標，將該座標紀錄為走過，並繼續走訪相鄰座標直到超出邊界或已經走過
# 注意遞迴時還是要再次檢查該座標是否為0或被走過grid[i][j] == '0' or self.visited[i][j]

class Solution(object):        
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        res = 0
        self.row = len(grid)
        self.col = len(grid[0])        
        self.visited = [[False for _ in range(self.col)] for _ in range(self.row)]
        
        for i in range(self.row):
            for j in range(self.col): 
                if grid[i][j] == '1' and not self.visited[i][j]:
                    self.dfs(i, j, grid)
                    res += 1
        
        return res
        
    def dfs(self, i, j, grid):
        if i < 0 or i >= self.row or j < 0 or j >= self.col or grid[i][j] == '0' or self.visited[i][j]:
            return None
        
        self.visited[i][j] = True

        self.dfs(i-1, j, grid)
        self.dfs(i+1, j, grid)
        self.dfs(i, j-1, grid)
        self.dfs(i, j+1, grid)
        
        return None
        

class Solution(object):        
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        res = 0
        self.row = len(grid)
        self.col = len(grid[0])        
        self.visited = [[False for _ in range(self.col)] for _ in range(self.row)]
        
        for i in range(self.row):
            for j in range(self.col): 
                res += self.dfs(i, j, grid)
        
        return res
        
    def dfs(self, i, j, grid):
        if i < 0 or i >= self.row or j < 0 or j >= self.col or grid[i][j] == '0' or self.visited[i][j]:
            return 0
        
        self.visited[i][j] = True

        # recursively visits all the adjacent positions of 1 but does't count islands
        self.dfs(i-1, j, grid)
        self.dfs(i+1, j, grid)
        self.dfs(i, j-1, grid)
        self.dfs(i, j+1, grid)
        
        # count islands
        return 1