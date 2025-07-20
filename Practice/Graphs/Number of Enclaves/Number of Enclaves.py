class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        """
        number of 1s which cannot be reached from a boundary 1
        traverse the grid from all the boundary 1s and update the value to 2
        traverse again to count remaining 1s
        """

        m = len(grid)
        n = len(grid[0])
        count = 0
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]

        def dfs(i, j):
            for dy, dx in directions:
                x = i + dx
                y = j + dy

                if 0 <= x < m and 0 <= y < n and grid[x][y] == 1:
                    grid[x][y] = 2
                    dfs(x, y)

        for i in range(m):
            for j in range(n):
                if (i == 0 or i == m - 1 or j == 0 or j == n - 1) and grid[i][j] == 1:
                    grid[i][j] = 2
                    dfs(i, j)

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    count += 1

        return count


# Time Complexity: O(m*n) - we traverse the grid multiple times
# Space Complexity: O(m*n) - for the recursion stack in the worst case
