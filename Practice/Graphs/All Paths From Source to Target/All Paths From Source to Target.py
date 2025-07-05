class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        destinationNode = len(graph) - 1
        ans = []
        visited = [False] * len(graph)

        if len(graph[0]) == 0:
            return ans

        def dfs(graph, current, node):
            # visited[node] = True
            if node == destinationNode:
                ans.append(list(current))
                return
            for neighbor in graph[node]:
                # if not visited[neighbor]:
                current.append(neighbor)
                dfs(graph, current, neighbor)
                current.pop()

        dfs(graph, [0], 0)

        return ans


# Time Complexity: O(2^n) where n is the number of nodes in the graph, as we can have exponential paths in the worst case.
# Space Complexity: O(n) for the recursion stack and the current path storage.
