class Solution(object):
    def helper(self, nums, index, prev_index, dp):
        # base case
        if index == len(nums):
            return 0

        if dp[index][prev_index]!=-1:
            return dp[index][prev_index]

        # pick
        pick = 0
        if prev_index==len(nums) or nums[index] > nums[prev_index]:
            pick = 1 + self.helper(nums, index+1, index, dp)

        # dontpick
        dont_pick = self.helper(nums, index+1, prev_index, dp)

        dp[index][prev_index] = max(pick, dont_pick)
        return dp[index][prev_index]

    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        dp = [1]*n

        for i in range(n):
            for j in range(i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i], 1+dp[j])

        return max(dp)