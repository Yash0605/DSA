class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # BFS solution  => level order traversal to get the minutes
        n, m = len(grid), len(grid[0])
        rotten = deque()
        fresh, minutes = 0, 0
        directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]

        for i in range(n):
            for j in range(m):
                if grid[i][j] == 2:
                    rotten.append((i, j))
                elif grid[i][j] == 1:
                    fresh += 1

        while rotten and fresh > 0:
            minutes += 1

            for _ in range(len(rotten)):
                x, y = rotten.popleft()

                for dy, dx in directions:
                    newX = x + dx
                    newY = y + dy

                    if 0 <= newX < n and 0 <= newY < m and grid[newX][newY] == 1:
                        rotten.append((newX, newY))
                        fresh -= 1
                        grid[newX][newY] = 2

        return minutes if fresh == 0 else -1
