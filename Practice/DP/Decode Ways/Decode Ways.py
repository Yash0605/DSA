class Solution:
    def helper(self, s, index, dp):
        # base case
        if index <= 0:
            return 1

        if dp[index] != -1:
            return dp[index]

        # single
        single, double = 0, 0
        if s[index] != "0":
            single = self.helper(s, index - 1, dp)

        # double
        if s[index - 1] == "1" or (s[index - 1] == "2" and s[index] < "7"):
            double = self.helper(s, index - 2, dp)

        dp[index] = single + double
        return dp[index]

    """
    Tabulation - Space optimiztion
    """

    def numDecodings(self, s: str) -> int:
        if s[0] == "0":
            return 0
        elif len(s) == 1:
            return 1

        prev2 = 1
        prev1 = 1
        curr = 0

        for i in range(2, len(s) + 1):
            curr = 0
            if s[i - 1] != "0":
                curr = prev1
            if s[i - 2] == "1" or (s[i - 2] == "2" and s[i - 1] < "7"):
                curr += prev2

            prev2 = prev1
            prev1 = curr

        return curr

    """
    Tabulation
    def numDecodings(self, s: str) -> int:
        if s[0] == "0":
            return 0
        elif len(s) == 1:
            return 1

        dp = [0] * (len(s)+1)
        dp[0] = 1
        dp[1] = 1

        for i in range(2, len(dp)):
            if s[i-1]!='0':
                dp[i] = dp[i-1]
            if s[i-2]=='1' or (s[i-2] == '2' and s[i-1] < '7'):
                dp[i] += dp[i-2]

        return dp[len(s)]
    """

    """
    Memoization
    def numDecodings(self, s: str) -> int:
        if s[0] == "0":
            return 0
        elif len(s) == 1:
            return 1

        dp = [-1] * (len(s))

        return self.helper(s, len(s) - 1, dp)
    """


# if started from index 0, then we can take the last digit as single digit or the last two digits as double digit.
# if the last digit is 0, then we can only take the last two digits as double digit


def decodeHelper(self, s, index, dp):
    if index >= len(s):
        return 1

    if dp[index] != -1:
        return dp[index]

    single, double = 0, 0

    # single char
    if s[index] != "0":
        single = self.decodeHelper(s, index + 1, dp)

    # double char
    if index < len(s) - 1 and (
        s[index] == "1" or (s[index] == "2" and s[index + 1] < "7")
    ):
        double = self.decodeHelper(s, index + 2, dp)

    dp[index] = single + double
    return dp[index]
