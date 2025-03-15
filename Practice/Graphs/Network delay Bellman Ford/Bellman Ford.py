class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        """
        Bellman Ford - If we relax all the edges n-1 times we should get the answer
        A=>B=>C => Dis to reach C => distance(B)+cost(BC) => relaxation"
        """

        distanceList = [float("inf")] * (n + 1)
        distanceList[0] = float(
            "-inf"
        )  # setting the 0th index to min value as the given nodes are 1 based index
        distanceList[k] = 0

        for i in range(n):
            for u, v, w in times:

                if distanceList[v] > distanceList[u] + w:
                    distanceList[v] = distanceList[u] + w

        # print(distanceList)
        ans = max(distanceList)

        return ans if ans != float("inf") else -1
