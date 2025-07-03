class Solution(object):
    def countLongest(self, s, i, j, dp):
        # base case
        if i == j:
            return 1

        if j < i:
            return 0

        if dp[i][j] != -1:
            return dp[i][j]

        # case where char i == char j => check if middle is pal or not
        if s[i] == s[j]:
            dp[i][j] = 2 + self.countLongest(s, i + 1, j - 1, dp)
            return dp[i][j]
        else:
            dp[i][j] = max(
                self.countLongest(s, i, j - 1, dp), self.countLongest(s, i + 1, j, dp)
            )
            return dp[i][j]

    def longestPalindromeSubseq(self, s):
        """
        :type s: str
        :rtype: int
        """
        """
        Using the Longest palindromic substring solution
        """
        dp = [[-1] * (len(s)) for _ in range(len(s))]
        return self.countLongest(s, 0, len(s) - 1, dp)


# Time Complexity: O(n^2) where n is the length of the string.
# Space Complexity: O(n^2) for the dp array.


class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        n = len(s)
        dp = [[0] * n for _ in range(n)]

        for l in range(1, n + 1):
            for i in range(n - l + 1):
                j = i + l - 1
                if i == j:
                    dp[i][j] = 1

                elif s[i] == s[j]:
                    dp[i][j] = 2 + dp[i + 1][j - 1]

                elif s[i] != s[j]:
                    dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])

        return dp[0][n - 1]


# Time Complexity: O(n^2) where n is the length of the string.
# Space Complexity: O(n^2) for the dp array.
