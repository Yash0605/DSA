class Solution:
    def resultingString(self, s: str) -> str:
        """
        Since we need to check the string again till all the adjacent chars are removed we can choose recursion
        But no overlapping subproblems will be available as we need to start fresh after removals
        also how to maintain index if the string keeps changing?
        Use combination of while and for loop => while to check if final string found and for to check in current string
        Still high TLE => can be solved with Stack
        """
        """
        strList = list(s)
        changedFlag = True

        # empty final string
        while changedFlag:
            changedFlag = False
            for i in range(1,len(strList)):
                if abs(ord(strList[i-1]) - ord(strList[i])) == 1 or abs(ord(strList[i-1]) - ord(strList[i])) == 25:
                    changedFlag = True
                    del strList[i-1:i+1]
                    break

        return "".join(strList)
        """

        stack = []

        for char in s:
            if stack:
                top = stack[-1]
                diff = abs(ord(top) - ord(char))
                if diff == 1 or diff == 25:
                    stack.pop()
                    continue

            stack.append(char)

        return "".join(stack)


# Time Complexity: O(n) where n is the length of the string
# Space Complexity: O(n) for the stack
