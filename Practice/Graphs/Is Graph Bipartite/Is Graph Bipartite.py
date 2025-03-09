# BFS solution to check if graph is bipartite or not
from collections import deque


class Solution(object):
    def isBipartite(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: bool
        """
        # BFS solution unvisited - 0 , color 1 and 2
        n = len(graph)
        visitedNodes = [0] * n
        q = deque()

        # since graph can be disconnected as well
        for i in range(n):
            if visitedNodes[i] == 0:
                q.append((i, 1))

                while len(q) > 0:
                    current_node, color = q.popleft()
                    visitedNodes[current_node] = color

                    for neighbor in graph[current_node]:
                        # if not visisted
                        if visitedNodes[neighbor] == 0:
                            q.append((neighbor, 2 if color == 1 else 1))
                        # if visited
                        elif visitedNodes[neighbor] != 0:
                            if visitedNodes[neighbor] == color:
                                return False

        return True


# DFS solution to check if graph is bipartite or not
class Solution:
    def checkBipartiteUtil(self, graph, visited, current, color):
        visited[current] = color

        for neighbor in graph[current]:
            if visited[neighbor] == -1:
                # this can return False so we need to check and return from here itself
                if not self.checkBipartiteUtil(graph, visited, neighbor, 1 - color):
                    return False
            elif visited[neighbor] == color:
                # The neighbor has the same color so cannot be Bipartite
                return False

        return True

    def isBipartite(self, graph: List[List[int]]) -> bool:
        # DFS
        # -1 for unvisited and 0 and 1 will be the colors
        n = len(graph)
        visited = [-1] * n

        # graph can be disconnected so traverse all the nodes
        for i in range(n):
            if visited[i] == -1:
                # this can return False so we need to check and return from here itself
                if not self.checkBipartiteUtil(graph, visited, i, 1):
                    return False

        return True
