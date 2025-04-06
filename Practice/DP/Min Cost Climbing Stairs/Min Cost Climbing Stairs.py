class Solution(object):
    def helper(self, cost, n, dp):
        if n <= 1:
            return 0

        if dp[n] != -1:
            return dp[n]

        dp[n] = min(
            self.helper(cost, n - 1, dp) + cost[n - 1],
            self.helper(cost, n - 2, dp) + cost[n - 2],
        )
        return dp[n]

    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        """
        we are considering n to be 1 based indexing and cost is 0 based index. 
        As per problem we need to find the cost of reaching top which is one step after the given steps
        So here n=3 means 4th index in case of cost => i.e 4th step
        cost of reaching 4th step = min(cost of reaching 3rd step + cost of 3rd step as we need 1 hop from this step to reach the top
        , cost of reaching 2nd step + cost of 2nd step)
        Here 3rd step cost => cost[2] and 2nd step cost => cost[1] => 0 based indexing
        """
        n = len(cost)
        # memoization
        # dp = [-1]*(len(cost)+1)
        # return self.helper(cost, n, dp)

        # tabulation
        dp = [0] * (len(cost) + 1)

        # for i in range(2, n+1):
        #     dp[i] = min(dp[i-1] + cost[i-1], dp[i-2]+ cost[i-2])

        # return dp[n]

        # tabulation space optimized
        prev1, prev2 = 0, 0
        ans = 0

        """
        Here 2 does not represent 2nd step but 2nd index in the cost list 
        so its the 3rd step which is being considered here
        """
        for i in range(2, n + 1):
            ans = min(prev1 + cost[i - 1], prev2 + cost[i - 2])
            prev2 = prev1
            prev1 = ans

        return ans
