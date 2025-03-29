# User function Template for python3
from typing import List


class DisjoinSet:
    def __init__(self, V):
        self.parent = [-1] * V
        for i in range(V):
            self.parent[i] = i

    def findParent(self, x):
        if self.parent[x] == x:
            return x

        # recursive call for the case where we have A->B->C and we are checking parent of C
        return self.findParent(self.parent[x])

    def Union(self, x, y):
        parX = self.findParent(x)
        parY = self.findParent(y)

        # union is not possible
        if parX == parY:
            return False

        self.parent[parX] = parY

        return True


class Solution:

    # Function to find sum of weights of edges of the Minimum Spanning Tree.
    def spanningTree(self, V: int, adj: List[List[int]]) -> int:
        # code here
        """
        Using Kruskal's algo
        Disjoint Set implemenation
        """
        ds = DisjoinSet(V)
        edges = []
        ans = 0

        """
        Input is in the form of adjacency list
        where for each node u we have connecting node v, w in the input
        [
        [(1,5), (2,1)], // node 0
        [(0,5), (2,3)], // node 1
        [(1,3), (0,1)] //node 2
        ]
        """
        for u in range(V):
            for v, w in adj[u]:
                if (
                    u < v
                ):  # Since undirected graph based on the input which should consider node u and v combo only once
                    # creating edges with weights as first element to be able to sort the list
                    edges.append((w, u, v))

        edges.sort()

        for w, u, v in edges:
            if ds.findParent(u) != ds.findParent(v):
                ans += w
                ds.Union(u, v)

        return ans


# {
# Driver Code Starts
# Initial Template for Python 3
import atexit
import io
import sys
from typing import List

# Contributed by : Nagendra Jha

if __name__ == "__main__":
    test_cases = int(input())
    for cases in range(test_cases):
        V = int(input())
        E = int(input())
        adj = [[] for i in range(V)]
        for i in range(E):
            u, v, w = map(int, input().strip().split())
            adj[u].append([v, w])
            adj[v].append([u, w])
        ob = Solution()

        print(ob.spanningTree(V, adj))
        print("~")

# } Driver Code Ends
