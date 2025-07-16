class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        numberOfClosedIslands = 0
        m,n = len(grid), len(grid[0])
        directions = [(-1, 0), (0,1), (1,0), (0,-1)]
        visited = [[False]*n for _ in range(m)]

        def dfs(i,j):
            if visited[i][j] or grid[i][j] == 1:
                return

            visited[i][j] = True

            for x,y in directions:
                if 0<=i+x<m and 0<=j+y<n and grid[i+x][j+y] == 0:
                    dfs(i+x, j+y)

        # flood fill cell removal i.e marked as visited 
        for i in range(m):
            for j in range(n):
                if i==0 or i==m-1 or j==0 or j==n-1 and grid[i][j] == 0:
                    dfs(i,j)

        for i in range(m):
            for j in range(n):
                if 0<i<m-1 and 0<j<n-1 and grid[i][j] == 0 and not visited[i][j]:
                    numberOfClosedIslands+=1
                    dfs(i,j)
                    
        return numberOfClosedIslands