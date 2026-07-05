class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows = len(grid)
        cols = len(grid[0])

        #maintain visited
        visited = [[0] * cols for _ in range(rows)]
        n_islands = 0
        for i in range(0,rows):
            for j in range(0,cols):
                if grid[i][j] == "1" and visited[i][j] == 0:
                    self.dfs(i,j,grid,visited)
                    n_islands += 1
        return n_islands
    
    def dfs(self,i,j,grid,visited):
        rows = len(grid)
        cols = len(grid[0])
        condition = (i>=0 and j>=0 and i<rows and j<cols)
        
        if not(condition) or grid[i][j] == "0" or visited[i][j] == 1:
            return
        
        visited[i][j] = 1

        neighbors = [(i+1,j),(i,j+1),(i-1,j),(i,j-1)]

        for (r,c) in neighbors:
            self.dfs(r,c,grid,visited)