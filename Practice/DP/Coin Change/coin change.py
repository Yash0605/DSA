class Solution(object):
    def coinChangeHelper(self, coins, amount, index, dp):
        # base case
        if amount == 0:
            return 0

        if index < 0:
            return float("inf")

        if dp[index][amount] != -1:
            return dp[index][amount]

        # pick
        pick = float("inf")
        if amount >= coins[index]:
            pick = 1 + self.coinChangeHelper(coins, amount - coins[index], index, dp)

        dont_pick = self.coinChangeHelper(coins, amount, index - 1, dp)

        dp[index][amount] = min(pick, dont_pick)
        return dp[index][amount]

    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        n = len(coins)
        coins.sort()

        # dp = [[-1]*(amount+1) for _ in range(n)]
        # val = self.coinChangeHelper(coins, amount, n-1, dp)
        # return val if val != float('inf') else -1

        dp = [[float("inf")] * (amount + 1) for _ in range(n)]

        dp[0][0] = 0

        # base case
        for i in range(amount + 1):
            if i >= coins[0]:
                if i % coins[0] == 0:
                    dp[0][i] = i // coins[0]

        for i in range(1, n):
            dp[i][0] = 0

        for i in range(1, n):
            for j in range(1, amount + 1):
                # pick
                if j >= coins[i]:
                    dp[i][j] = 1 + dp[i][j - coins[i]]

                dp[i][j] = min(dp[i][j], dp[i - 1][j])

        # print(dp)
        return dp[n - 1][amount] if dp[n - 1][amount] != float("inf") else -1
