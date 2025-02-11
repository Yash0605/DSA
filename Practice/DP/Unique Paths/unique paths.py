class Solution(object):
    def helper(self, m, n, i, j,dp):
        # base case
        if i>=m or j>=n:
            return 0

        if i==m-1 and j==n-1:
            return 1

        if dp[i][j]!=-1:
            return dp[i][j]

        # go right
        right = self.helper(m,n,i,j+1,dp)

        # go down
        down = self.helper(m,n,i+1,j,dp)

        dp[i][j] = right+down
        return dp[i][j]

    '''
    Tabulation
    '''
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int

        A cell in DP signifies the number of possible unique paths that the robot can take to reach that cell
        A robot can reach the cell either from top or left 
        """
        dp = [[-1]*n for i in range(m)]

        # initial conditions - for the 1st row and col there is only 1 path to reach the cells
        for i in range(m):
            dp[i][0] = 1

        for j in range(n):
            dp[0][j] = 1

        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i-1][j]+dp[i][j-1]

        return dp[m-1][n-1]

    '''
    Memoization
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        dp = [[-1]*n for i in range(m)]
        return self.helper(m,n,0,0,dp)
    '''
        