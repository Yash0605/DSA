class Solution {
    private int helper(int[] nums, int index, int[] dp) {
        if(index >= nums.length) {
            return 0;
        }

        if(dp[index]!=-1) {
            return dp[index];
        }

        int pick = helper(nums, index+2, dp) + nums[index];
        int dontPick = helper(nums, index+1, dp);

        dp[index] = Math.max(pick, dontPick);
        return dp[index];
    }

    public int rob(int[] nums) {
        // Basic recusrion
        // return helper(nums, 0);

        int[] dp = new int[nums.length];

        /*
        Memoization

        for(int i=0; i<nums.length; i++){
            dp[i] = -1;
        }

        return helper(nums, 0, dp);
        */

        // Tabulation
        if(nums.length == 1) return nums[0];

        dp[0] = nums[0];
        dp[1] = Math.max(nums[0], nums[1]);

        for(int i=2; i<nums.length; i++){
            int pick = dp[i-2]+nums[i];
            int dontPick = dp[i-1];

            dp[i] = Math.max(pick, dontPick);
        }

        return dp[nums.length-1];
    }
}

// Time Complexity: O(n)
// Space Complexity: O(n) for memoization and tabulation, O(1) for space optimization