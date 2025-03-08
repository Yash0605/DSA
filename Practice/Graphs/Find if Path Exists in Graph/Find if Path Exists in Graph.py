from collections import defaultdict


class Solution:
    def traverseNodes(self, n, adjacency_list, source, destination, visited_nodes):
        # base case
        if source == destination:
            return True

        visited_nodes[source] = True

        # using adjacency_matrix
        # traversing the neighbours => since matrix we need to check all n and then check if 1
        # for i in range(n):
        #     if adjacency_matrix[source][i] and not visited_nodes[i]:
        #         if self.traverseNodes(n, adjacency_matrix, i, destination, visited_nodes):
        #             return True

        for neighbour in adjacency_list[source]:
            if not visited_nodes[neighbour]:
                # need to check if that neighboure can reach the destination => if so we will simply return
                if self.traverseNodes(
                    n, adjacency_list, neighbour, destination, visited_nodes
                ):
                    return True

        return False

    def validPath(
        self, n: int, edges: List[List[int]], source: int, destination: int
    ) -> bool:
        # using adjacency matrix
        # adjacency_matrix = [[0] * n for _ in range(n)]

        adjacency_list = defaultdict(list)
        visited_nodes = [False] * n

        for edge in edges:
            u, v = edge[0], edge[1]
            adjacency_list[u].append(v)
            adjacency_list[v].append(u)

        return self.traverseNodes(n, adjacency_list, source, destination, visited_nodes)
