class Solution:
    def countSubstringsHelper(self, s, i, j, dp):
        if dp[i][j] != -1:
            return dp[i][j]

        if i == j:
            dp[i][j] = True
            return True

        if j < i:
            return False

        # case ele at i and j are different
        self.countSubstringsHelper(s, i, j - 1, dp)
        self.countSubstringsHelper(s, i + 1, j, dp)

        if s[i] == s[j] and (
            j == i + 1 or self.countSubstringsHelper(s, i + 1, j - 1, dp)
        ):
            dp[i][j] = True
            return dp[i][j]

        dp[i][j] = False
        return dp[i][j]

    def countSubstrings(self, s: str) -> int:
        n = len(s)
        ans = 0
        dp = [[-1] * n for _ in range(n)]

        self.countSubstringsHelper(s, 0, n - 1, dp)

        # once the dp is populated we need to check which cells have the value as True
        #  2 ways either chck row wise or diagonally
        # way 1
        """
        for i in range(n):
            for j in range(n):
                if dp[i][j] == True:
                    ans+=1
        """

        #  way 2
        """
        for length in range(1,n+1):
            for i in range(n-length+1):
                j=i+length-1
                if dp[i][j] == True:
                    ans+=1
        """

        # Gap Strategy
        for length in range(1, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1

                # 1 char
                if i == j:
                    dp[i][j] = True
                else:
                    # 2 chars
                    if j == i + 1:
                        dp[i][j] = s[i] == s[j]
                    else:
                        if s[i] == s[j]:
                            dp[i][j] = dp[i + 1][j - 1]
                        # no need to check for this case as here we are checking if any dp[i][j - 1] or dp[i + 1][j] is palindrome
                        # but since these are already populated we have checked this once already this will cause dups
                        # else:
                        #     dp[i][j] = dp[i][j - 1] or dp[i + 1][j]

                if dp[i][j] == True:
                    ans += 1

        return ans


# Time Complexity: O(n^2) where n is the length of the string
# Space Complexity: O(n^2) for the dp array
