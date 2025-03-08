class Solution:
    def isSafe(self, neighbor_i, neighbor_j, m, n):
        return neighbor_i >= 0 and neighbor_i < m and neighbor_j >= 0 and neighbor_j < n

    def connectCells(self, grid, visitedCells, i, j, m, n):
        visitedCells[i][j] = True

        # we need to check neigbouring cells => we can check in 4 directions
        # for a cell i,j it will be => [(i-1,j),(i, j+1),(i+1,j),(i,j-1)]
        deltaDirection = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        for k in range(4):
            neighbor_i = i + deltaDirection[k][0]
            neighbor_j = j + deltaDirection[k][1]

            if (
                self.isSafe(neighbor_i, neighbor_j, m, n)
                and grid[neighbor_i][neighbor_j] == "1"
                and not visitedCells[neighbor_i][neighbor_j]
            ):
                self.connectCells(grid, visitedCells, neighbor_i, neighbor_j, m, n)

    def numIslands(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])
        visitedCells = [[False] * n for _ in range(m)]
        islands = 0

        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1" and not visitedCells[i][j]:
                    islands += 1
                    self.connectCells(grid, visitedCells, i, j, m, n)

        return islands
