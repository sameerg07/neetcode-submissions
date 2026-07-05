class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])

        visited = [[0] * cols for _ in range(rows)]
        max_island_area = 0

        for i in range(rows):
            for j in range(cols):
                if visited[i][j] == 0 and grid[i][j] == 1:
                    print("processing {i}:{j}",i,j)
                    island_area = self.dfs(i,j,grid,visited, 0)
                    max_island_area = max(island_area,max_island_area)
        return max_island_area
        

    def dfs(self,i,j,grid,visited,area):
        rows = len(grid)
        cols = len(grid[0])

        condition = (i>=0 and j>=0 and i<rows and j<cols)

        if not(condition) or grid[i][j] == 0 or visited[i][j] == 1:
            return area

        visited[i][j] = 1
        area = area + 1
        
        neighbors = [(i,j+1),(i,j-1),(i-1,j),(i+1,j)]

        for (r,c) in neighbors:
            area = self.dfs(r,c,grid,visited,area)
        return area
