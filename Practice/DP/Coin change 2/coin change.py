class Solution(object):
    def changeHelper(self, amount, coins, index, dp):
        if amount == 0:
            return 1

        if index == len(coins):
            return 0

        if dp[index][amount] != -1:
            return dp[index][amount]

        # select
        pick = 0
        if amount >= coins[index]:
            pick += self.changeHelper(amount - coins[index], coins, index, dp)

        skip = self.changeHelper(amount, coins, index + 1, dp)

        dp[index][amount] = pick + skip
        return dp[index][amount]

    def change(self, amount, coins):
        """
        :type amount: int
        :type coins: List[int]
        :rtype: int
        """
        # return self.changeHelper(amount, coins, 0)

        # memoization
        # dp = [[-1]*(amount+1) for _ in range(len(coins))]
        # return self.changeHelper(amount, coins, 0, dp)

        # Tabulation
        dp = [[0] * (amount + 1) for _ in range(len(coins))]

        for i in range(len(coins)):
            dp[i][0] = 1

        for i in range(1, amount + 1):
            if i == coins[0]:
                dp[0][i] = 1
            elif i > coins[0]:
                dp[0][i] = 1 if i % coins[0] == 0 else 0

        for i in range(1, len(coins)):
            for j in range(1, amount + 1):
                pick = 0
                if j >= coins[i]:
                    pick = dp[i][j - coins[i]]

                skip = dp[i - 1][j]

                dp[i][j] = pick + skip

        # print(dp)
        return dp[len(coins) - 1][amount]
# Time Complexity: O(n * amount) where n is the number of coins
# Space Complexity: O(n * amount) for the dp array