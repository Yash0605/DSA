class Solution(object):
    def isMatchHelper(self, s, p, index1, index2, dp):
        # base case
        # both finished
        if index1 == len(s) and index2 == len(p):
            return True
        # s finsihed
        if index1 == len(s):
            if p[index2] == "*":
                return self.isMatchHelper(s, p, index1, index2 + 1, dp)
            else:
                return False
        # p finished
        if index2 == len(p) and index1 < len(s):
            return False

        if dp[index1][index2] != -1:
            return dp[index1][index2]

        # case chars are same or ?
        if s[index1] == p[index2] or p[index2] == "?":
            dp[index1][index2] = self.isMatchHelper(s, p, index1 + 1, index2 + 1, dp)
            return dp[index1][index2]
        else:
            if p[index2] == "*":
                dp[index1][index2] = self.isMatchHelper(
                    s, p, index1, index2 + 1, dp
                ) or self.isMatchHelper(s, p, index1 + 1, index2, dp)
                return dp[index1][index2]
            else:
                dp[index1][index2] = False
                return dp[index1][index2]

    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        # dp = [[-1]*len(p) for _ in range(len(s))]
        # return self.isMatchHelper(s, p, 0, 0, dp)

        # Tabulation
        dp = [[False] * (len(p) + 1) for _ in range(len(s) + 1)]
        dp[0][0] = True

        if len(p) == 1:
            if p[0] == "*":
                dp[0][1] = True

        for i in range(1, len(p) + 1):
            if p[i - 1] == "*":
                if i == 1:
                    dp[0][i] = True
                else:
                    dp[0][i] = dp[0][i - 1]
            else:
                dp[0][i] = False

        # print(dp)

        for i in range(1, len(s) + 1):
            for j in range(1, len(p) + 1):
                if s[i - 1] == p[j - 1] or p[j - 1] == "?":
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    if p[j - 1] == "*":
                        dp[i][j] = dp[i][j - 1] or dp[i - 1][j]
                    else:
                        dp[i][j] = False

        # print(dp)
        return dp[len(s)][len(p)]
