class Solution:
    def helper(self, prices, k, index, dp):
        # base case
        if k<=0 or index == len(prices):
            return 0

        if dp[index][k]!=-1:
            return dp[index][k]

        # dont pick
        dont_pick = self.helper(prices, k, index+1, dp)

        # pick
        pick = 0
        for i in range(index+1, len(prices)):
            pick = max(pick, prices[i] - prices[index] + self.helper(prices, k-1, i+1, dp))

        dp[index][k] = max(pick, dont_pick)
        return dp[index][k]
        

    '''
    Tabulation
    '''

    def maxProfit(self, k: int, prices: List[int]) -> int:
        n = len(prices)
        # dp = [[0]*(k+1) for _ in range(n)]
        dp = [[0]*n for _ in range(k+1)]

        '''
        A cell in dp stores the profit till that day => which means we would have sold the stock on that day
        => this means it would have been bought earlier -> thus need to check the profit val for all the earlier days as buying day
        => once the buy day found we will have to consider the subproblem that what was profit till that buying day with 1 lesser trxn
        '''
        
        for i in range(1,k+1):
            for j in range(1,n):
                # dont pick - prev day but same number of trxn
                dont_pick = dp[i][j-1]

                # pick
                pick=0
                for m in range(j):
                    # pick is for the case if sold on ith day and bought on mth day + whatever was the profit till mth day for 1 lesser trxn 
                    if prices[m] < prices[j]:
                        pick = max(pick, prices[j] - prices[m] + dp[i-1][m])

                dp[i][j] = max(pick, dont_pick)

        return dp[k][n-1]

    '''
    Memoization

    def maxProfit(self, k: int, prices: List[int]) -> int:
        n = len(prices)
        dp = [[-1]*(k+1) for _ in range(n)]
        return self.helper(prices, k, 0, dp)
    '''