class Solution(object):
    def countSquares(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        n = len(matrix)
        m = len(matrix[0])
        dp = [row[:] for row in matrix]
        ans = sum(dp[0])

        for j in range(1,n):
            ans+=dp[j][0]

        for i in range(1,n):
            for j in range(1,m):
                if dp[i][j] == 1:
                    dp[i][j] = 1+min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1])

                ans+=dp[i][j]

        return ans

# Time Complexity: O(n*m)
# Space Complexity