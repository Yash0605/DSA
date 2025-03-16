import heapq
from collections import defaultdict


class Solution(object):
    def networkDelayTime(self, times, n, k):
        """
        :type times: List[List[int]]
        :type n: int
        :type k: int
        :rtype: int
        """
        """
        Using Dijkstras Algo
        We need to form a priority queue and need to keep a distance list to keep track of the min distance for each node

        """
        distanceList = [float("inf")] * (n + 1)
        distanceList[k] = 0
        graph = defaultdict(list)

        # form the adjacency list for traversal
        for u, v, w in times:
            graph[u].append((v, w))

        q = []
        heapq.heapify(q)
        heapq.heappush(q, (0, k))

        while len(q) > 0:
            currentDistance, currentNode = heapq.heappop(
                q
            )  # currentDistance is only present to help us sort the priority queue

            for neighbor, neighborDistance in graph[currentNode]:
                if (
                    distanceList[neighbor]
                    > distanceList[currentNode] + neighborDistance
                ):
                    distanceList[neighbor] = (
                        distanceList[currentNode] + neighborDistance
                    )
                    heapq.heappush(q, (distanceList[neighbor], neighbor))

        ans = float("-inf")
        for i in range(1, n + 1):
            ans = max(ans, distanceList[i])

        return ans if ans != float("inf") else -1
