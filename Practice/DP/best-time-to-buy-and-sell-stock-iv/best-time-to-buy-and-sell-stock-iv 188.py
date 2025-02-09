class Solution:
    def helper(self, prices, k, index):
        # base case
        if k<=0 or index == len(prices):
            return 0

        # dont pick
        dont_pick = self.helper(prices, k, index+1)

        # pick
        pick = 0
        for i in range(index+1, len(prices)):
            pick = max(pick, prices[i] - prices[index] + self.helper(prices, k-1, i))

        return max(pick, dont_pick)
        

    def maxProfit(self, k: int, prices: List[int]) -> int:
        return self.helper(prices, k, 0)