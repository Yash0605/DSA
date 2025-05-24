class Solution:
    def knapsackHelper(self, W, val, wt, index, dp):
        # base case
        if W<=0 or index == len(wt):
            return 0
        
        if dp[index][W]!=-1:
            return dp[index][W]
        # pick the weight
        pick=0
        
        if wt[index] <= W:
            pick += val[index] + self.knapsackHelper(W-wt[index], val, wt, index+1, dp)
            
        dont_pick = self.knapsackHelper(W, val, wt, index+1, dp)
        
        dp[index][W] = max(pick, dont_pick)
        return dp[index][W]
    
    def knapsack(self, W, val, wt):
        # code here
        # dp = [[-1]*(W+1) for i in range(len(wt))]
        # return self.knapsackHelper(W, val, wt, 0, dp)
        
        n = len(wt)
        
        dp = [[0]*(W+1) for i in range(len(wt))]
        
            
        for i in range(wt[0], W+1):
            if i<= W:
                dp[0][i] = val[0]
            
            
        for i in range(1, len(wt)):
            for j in range(1, W+1):
                pick = 0
                
                if wt[i] <= j:
                    pick = val[i] + dp[i-1][j-wt[i]]
                    
                dont_pick = dp[i-1][j]
                
                dp[i][j] = max(pick, dont_pick)
                
        return dp[n-1][W]