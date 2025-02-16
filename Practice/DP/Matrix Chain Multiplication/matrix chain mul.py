class Solution:
    def matrixMultiplication(self, arr):
        # code here
        n = len(arr)
        dp = [[float('inf')]*(n) for _ in range(n)]
        
        
        for l in range(1,n):
            for i in range(1,n-l+1):
                j = i+l-1
                
                if j==i:
                    dp[i][j] = 0
                
                elif j==i+1:
                    dp[i][j] = arr[i-1]*arr[i]*arr[j]
                    
                else:
                    
                    for k in range(i,j):
                        dp[i][j] = min(dp[i][j], dp[i][k]+dp[k+1][j]+arr[i-1]*arr[k]*arr[j])
                        
        return dp[1][n-1]

# Time Complexity: O(n^3) - check once
# Space Complexity: O(n^2)