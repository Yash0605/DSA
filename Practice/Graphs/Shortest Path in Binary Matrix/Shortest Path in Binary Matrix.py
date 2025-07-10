from collections import deque

class Solution(object):
    def shortestPathBinaryMatrix(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        n = len(grid)
        if grid[0][0] == 1 or grid[n-1][n-1] == 1:
            return -1

        directions = [(-1, -1), (-1, 0), (-1, 1),
                      (0, -1),          (0, 1),
                      (1, -1), (1, 0),  (1, 1)]

        queue = deque([(0, 0, 1)])
        visited = set((0, 0))

        while queue:
            x, y, length = queue.popleft()

            if x == n - 1 and y == n - 1:
                return length

            for dx, dy in directions:
                newX, newY = x + dx, y + dy
                if 0 <= newX < n and 0 <= newY < n and grid[newX][newY] == 0 and (newX, newY) not in visited:
                    visited.add((newX, newY))
                    queue.append((newX, newY, length + 1))

        return -1
