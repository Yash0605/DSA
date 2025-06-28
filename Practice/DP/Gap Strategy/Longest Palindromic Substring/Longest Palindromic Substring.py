class Solution:
    def getPalindrome(self, s, i, j, ans):
        # base case

        if j < i:
            return False

        isPalindrome = False

        if i == j:
            isPalindrome = True
        elif s[i] == s[j] and (j == i + 1 or self.getPalindrome(s, i + 1, j - 1, ans)):
            isPalindrome = True

        if isPalindrome:
            if j - i + 1 > len(ans[0]):
                ans[0] = s[i : j + 1]
        else:
            self.getPalindrome(s, i, j - 1, ans)
            self.getPalindrome(s, i + 1, j, ans)

        return isPalindrome

    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        # ans = ['']
        # self.getPalindrome(s, 0, n - 1, ans)
        # return ans[0]

        ans = ""
        dp = [[False] * n for _ in range(n)]

        for length in range(1, n + 1):
            for i in range(0, n - length + 1):
                j = i + length - 1

                if i == j:
                    dp[i][j] = True
                    ans = s[i]
                else:
                    # no need to check for case where s[i] != s[j] as then we need to check if substring are palindrome or not and this check would already have been done
                    if s[i] == s[j] and (j == i + 1 or dp[i + 1][j - 1]):
                        dp[i][j] = True
                        ans = s[i : j + 1]

        return ans


# Time Complexity: O(n^2) where n is the length of the string
# Space Complexity: O(n^2) for the dp array
