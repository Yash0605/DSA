class Solution(object):
    def countWays(self, obstacleGrid, m, n, i, j, dp):
        if i == 0 and j == 0:
            return 1 if obstacleGrid[i][j] == 0 else 0

        if i < 0 or j < 0 or obstacleGrid[i][j] == 1:
            return 0

        if dp[i][j] != -1:
            return dp[i][j]

        # can reach the current cell from top
        top = self.countWays(obstacleGrid, m, n, i - 1, j, dp)

        # or can reach from left
        left = self.countWays(obstacleGrid, m, n, i, j - 1, dp)

        dp[i][j] = top + left
        return top + left

    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])

        # dp = [[-1]*(n) for _ in range(m)]

        # if m-1==0 and n-1==0:
        #     return 1 if obstacleGrid[m-1][n-1] == 0 else 0

        # return self.countWays(obstacleGrid, m-1, n-1, m-1, n-1, dp)

        dp = [[0] * (n) for _ in range(m)]

        if obstacleGrid[0][0] == 1:
            return 0

        dp[0][0] = 1

        for i in range(1, n):
            if obstacleGrid[0][i] != 1:
                dp[0][i] = 1 if dp[0][i - 1] == 1 else 0

        for j in range(1, m):
            if obstacleGrid[j][0] != 1:
                dp[j][0] = 1 if dp[j - 1][0] == 1 else 0

        for i in range(1, m):
            for j in range(1, n):
                if obstacleGrid[i][j] != 1:
                    dp[i][j] = dp[i - 1][j] + dp[i][j - 1]

        # print(dp)
        return dp[m - 1][n - 1]


# Time Complexity: O(m*n)
# Space Complexity: O(m*n) for the dp array
# Space Complexity: O(n) if we use only 2 rows for dp
# Space Complexity: O(1) if we use only 2 rows for dp and update the grid in place
