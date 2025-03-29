from collections import defaultdict


class Solution:
    def findCheapestPrice(
        self, n: int, flights: List[List[int]], src: int, dst: int, k: int
    ) -> int:
        # Bellman Ford
        distanceList = [float("inf")] * len(flights)
        distanceList[src] = 0

        for i in range(k + 1):
            """
            w/o temp:
            Suppose we update cost[flightDest] directly. If flightDest is later used as flightSrc in the same iteration,
            the new cost (updated in this round)might affect subsequent calculations incorrectly.

            temp ensures that updates in the current iteration don’t interfere with other edge relaxations happening in the same iteration.
            """
            temp = distanceList[:]
            for u, v, w in flights:
                temp[v] = min(temp[v], distanceList[u] + w)

            distanceList = temp[:]

        return distanceList[dst] if distanceList[dst] != float("inf") else -1
