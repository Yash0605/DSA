class Solution:
    def findWays(self, denominations, amount, index, dp):
        # base case
        if amount == 0:
            return 1

        if index == len(denominations):
            return 0

        if dp[amount][index] != -1:
            return dp[amount][index]

        # select the current denomination
        pick = 0
        if denominations[index] <= amount:
            pick = self.findWays(
                denominations, amount - denominations[index], index, dp
            )

        dontPick = self.findWays(denominations, amount, index + 1, dp)

        dp[amount][index] = pick + dontPick
        return dp[amount][index]

    def findCoins(self, numWays: List[int]) -> List[int]:
        denominations = []

        for i in range(len(numWays)):
            # if numWays[i] != 0:
            if len(denominations) > 0:
                dp = [[-1] * len(denominations) for _ in range(i + 2)]
                possibleWays = self.findWays(denominations, i + 1, 0, dp)

                if possibleWays > 0 and numWays[i] == 0:
                    return []
                elif possibleWays == numWays[i] - 1:
                    denominations.append(i + 1)
                elif possibleWays < numWays[i] - 1:
                    return []
            else:
                if numWays[i] == 1:
                    # check if all previous values are 0 as well
                    for j in range(i):
                        if numWays[j] > 0:
                            return []
                    denominations.append(i + 1)

        return denominations


# TC = O(n * m), where n is the amount and m is the number of denominations
# SC = O(n * m), where n is the amount and m is the number of denominations
