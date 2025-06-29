class Solution:

    def countPrefix(self, a, b):
        minLen = min(len(a), len(b))
        maxPrefix = 0

        for i in range(minLen):
            if a[i] == b[i]:
                maxPrefix += 1
            else:
                break

        return maxPrefix

    def longestCommonPrefix(self, words: List[str]) -> List[int]:
        n = len(words)
        ans = [0] * n
        prefix, suffix = [0] * n, [0] * n

        if n == 1:
            return [0]

        for i in range(1, n):
            prefix[i] = max(prefix[i - 1], self.countPrefix(words[i], words[i - 1]))

        for i in range(n - 2, -1, -1):
            suffix[i] = max(suffix[i + 1], self.countPrefix(words[i], words[i + 1]))

        for i in range(n):
            if i == 0:
                ans[i] = suffix[i + 1]
                continue

            if i == n - 1:
                ans[i] = prefix[i - 1]
                break

            ans[i] = max(
                prefix[i - 1],
                suffix[i + 1],
                self.countPrefix(words[i - 1], words[i + 1]),
            )
        return ans


# Time Complexity: O(n * m) where n is the number of words and m is the average length of the words.
# Space Complexity: O(n) for the prefix and suffix arrays.
