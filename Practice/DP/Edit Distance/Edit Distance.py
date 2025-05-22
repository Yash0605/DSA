class Solution(object):
    def minDistanceHelper(self, word1, word2, index1, index2, dp):
        # base case
        if index1 == len(word1) and index2 == len(word2):
            return 0

        if index1 == len(word1) and index2 < len(word2):
            return len(word2) - index2

        if index1 < len(word1) and index2 == len(word2):
            return len(word1) - index1

        if dp[index1][index2] != -1:
            return dp[index1][index2]

        if word1[index1] == word2[index2]:
            dp[index1][index2] = self.minDistanceHelper(
                word1, word2, index1 + 1, index2 + 1, dp
            )
            return dp[index1][index2]

        else:
            dp[index1][index2] = 1 + min(
                self.minDistanceHelper(word1, word2, index1 + 1, index2 + 1, dp),
                self.minDistanceHelper(word1, word2, index1 + 1, index2, dp),
                self.minDistanceHelper(word1, word2, index1, index2 + 1, dp),
            )
            return dp[index1][index2]

    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        n, m = len(word1), len(word2)
        # dp = [[-1]*m for i in range(n)]

        # return self.minDistanceHelper(word1, word2, 0, 0, dp)

        dp = [[0] * (m + 1) for i in range(n + 1)]
        dp[0][0] = 0

        for i in range(1, n + 1):
            dp[i][0] = i

        for i in range(1, m + 1):
            dp[0][i] = i

        for i in range(1, n + 1):
            for j in range(1, m + 1):
                if word1[i - 1] == word2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = 1 + min(dp[i - 1][j - 1], dp[i - 1][j], dp[i][j - 1])

        return dp[n][m]
