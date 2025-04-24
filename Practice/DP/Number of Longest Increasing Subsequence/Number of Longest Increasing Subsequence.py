class Solution(object):
    def findNumberOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        dp = [1] * n
        counts = [1] * n

        curr_max = 1
        cnt = 0

        for i in range(1, n):
            for j in range(i):
                if nums[i] > nums[j]:
                    # dp[i] = max(dp[i], dp[j]+1)

                    length_through_j = dp[j] + 1
                    if length_through_j > dp[i]:
                        dp[i] = length_through_j
                        counts[i] = counts[j]
                    elif length_through_j == dp[i]:
                        counts[i] += counts[j]
        # print(dp)

        result = 0
        curr_max = max(dp)
        for i in range(n):
            if dp[i] == curr_max:
                result += counts[i]

        return result
