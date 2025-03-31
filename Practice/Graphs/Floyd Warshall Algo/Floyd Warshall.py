class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # Using Floyd Warshall
        """
        Not ideal for this problem
        With this algo we can find shortest path from every node to every other node => multi source algo
        DP solution
        """
        graph = [[float("inf")] * n for _ in range(n)]

        # setting diagonals
        for i in range(n):
            for j in range(n):
                if i == j:
                    graph[i][j] = 0

        # setting values
        for u, v, w in times:
            graph[u - 1][v - 1] = w

        # finding the min value via p node
        for p in range(n):
            for i in range(n):
                for j in range(n):
                    graph[i][j] = min(graph[i][j], graph[i][p] + graph[p][j])

        # actual problem solution
        ans = -1
        for i in range(n):
            ans = max(ans, graph[k - 1][i])

        return ans if ans != float("inf") else -1
