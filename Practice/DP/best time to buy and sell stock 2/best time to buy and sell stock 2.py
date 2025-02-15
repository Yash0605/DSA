class Solution:
    def helper(self, prices, index, dp):
        if index == len(prices):
            return 0

        if dp[index] != -1:
            return dp[index]

        buy = 0
        for i in range(index + 1, len(prices)):
            buy = max(buy, prices[i] - prices[index] + self.helper(prices, i, dp))

        # not buy
        not_buy = self.helper(prices, index + 1, dp)

        dp[index] = max(buy, not_buy)

        return dp[index]

    """
    Final solution
    """

    def maxProfit(self, prices: List[int]) -> int:

        profit = 0

        '''
        Using Maths
        Suppose we have a increasing array => [1,3,5,7,9] => In this case profit will be when we do 9-1 = 8.
        But we can get the same ans if we do => 3-1+5-3+7-5+9-7 = 8
        Thus we can get the same val if we just do profit+=prices[i] - prices[i-1] for the case where prices[i] > prices[i-1]
        In case we get a decreasing sequence we can simply skip it and still get the same ans
        '''
        for i in range(1, len(prices)):
            if prices[i] > prices[i - 1]:
                profit += prices[i] - prices[i - 1]

        return profit

    """
    Tabulation
    

    def maxProfit(self, prices: List[int]) -> int:
        dp = [0] * len(prices)

        '''
        In the dp list each cell signifies what would be the profit 
            if the stock was bought at any of the earlier days and then sold at this ith day
            so j loop runs to get the prev buying day which could yield the max profit
            but this would only make sense if current price is greater than prev day price else we would already have the max profit
                - no need to check then at the current index hence the if condition
        '''

        for i in range(1, len(prices)):
            buy = 0

            if prices[i] > prices[i-1]:
                for j in range(i):
                    buy = max(buy, prices[i] - prices[j] + dp[j])

            # not buy
            not_buy = dp[i-1]

            dp[i] = max(buy, not_buy)

        return dp[len(prices)-1]
"""
    """
    Memoization

    def maxProfit(self, prices: List[int]) -> int:
        dp = [-1] * len(prices)
        return self.helper(prices, 0, dp)
    """
