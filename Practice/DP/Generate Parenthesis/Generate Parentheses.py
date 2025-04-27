class Solution(object):
    def parenthesisHelper(self, n, ans, open, close, current):
        if len(current) >= 2 * n:
            ans.append(current)
            current = ""
            return

        if open < n:
            self.parenthesisHelper(n, ans, open + 1, close, current + "(")

        if close < open:
            self.parenthesisHelper(n, ans, open, close + 1, current + ")")

    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        ans = []
        self.parenthesisHelper(n, ans, 0, 0, "")
        return ans
