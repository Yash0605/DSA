class Solution:
    def checkNeighbours(self, isConnected, visited, current, n):
        visited[current] = True

        for i in range(n):
            if i != current and isConnected[current][i] and not visited[i]:
                self.checkNeighbours(isConnected, visited, i, n)

    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        provinces = 0

        visited_cities = [False] * n

        for i in range(n):
            if not visited_cities[i]:
                provinces += 1
                # visited[i] = True
                self.checkNeighbours(isConnected, visited_cities, i, n)

        return provinces
