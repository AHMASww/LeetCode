'''
BFS和DFS都可，也可使用并查集
'''
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        
        row = len(grid)
        column = len(grid[0])
        land = 0
        self.visit = [[False for _ in range(column)] for _ in range(row)]
        
        for i in range(row):
            for j in range(column):
                if grid[i][j] == "1" and self.visit[i][j] == False:
                    self.BFS(grid, row, column, i, j)
                    land += 1
                    
        return land
    
    def BFS(self, grid, row, column, x, y):
        if x < 0 or x >= row or y < 0 or y >= column or self.visit[x][y] == True or grid[x][y] != "1":
            return
        
        self.visit[x][y] = True
        self.BFS(grid, row, column, x+1, y)
        self.BFS(grid, row, column, x, y+1)
        self.BFS(grid, row, column, x-1, y)
        self.BFS(grid, row, column, x, y-1)
