class DSU:
    def __init__(self, n):
        self.parent = [-1] * n
        for i in range(n):
            self.parent[i] = i

    def findParent(self, x):
        if self.parent[x] == x:
            return x

        return self.findParent(self.parent[x])

    def isUnion(self, x, y):
        parentX = self.findParent(x)
        parentY = self.findParent(y)

        if parentX == parentY:
            return False

        self.parent[parentX] = parentY
        return True


class Solution(object):
    # def getDistance(self,i,j):
    #     return abs(i[0] - j[0]) + abs(i[1] - j[1])

    def minCostConnectPoints(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        """
        Minimum spanning tree - Using Kruskal's algo
        => Union
        => Find Parent
        => requires external sort to get the min edge
        """
        getDistance = lambda i, j: abs(i[0] - j[0]) + abs(i[1] - j[1])
        edges = []
        dsu = DSU(len(points))

        for i in range(len(points)):
            for j in range(i + 1, len(points)):
                edges.append((getDistance(points[i], points[j]), i, j))

        edges.sort()

        ans = 0
        for i in range(len(edges)):
            w, u, v = edges[i]

            if dsu.isUnion(u, v):
                ans += w

        return ans


# Prims algo
import heapq
from collections import defaultdict


class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        """
        Since we need exactly 1 simple path, we can achieve this via creating a minimum spanning tree
        via Prim's => Priority Queue i.e min heap implementation
        """
        # creating the adjacency list
        adjList = [[float("inf")] * len(points) for _ in range(len(points))]

        for i in range(len(points)):
            pointA = points[i]
            for j in range(len(points)):
                if pointA != points[j]:
                    adjList[i][j] = abs(pointA[0] - points[j][0]) + abs(
                        pointA[1] - points[j][1]
                    )

        queue = []
        heapq.heapify(queue)
        heapq.heappush(queue, (0, 0))

        visited = [False] * len(points)
        ans = 0

        while len(queue) > 0:
            cost, node = heapq.heappop(queue)

            if visited[node]:
                continue

            visited[node] = True
            ans += cost

            for j in range(len(points)):
                heapq.heappush(queue, (adjList[node][j], j))

        return ans
