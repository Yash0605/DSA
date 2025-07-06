import java.util.ArrayList;
import java.util.List;

class Solution {
    private boolean dfs(List<List<Integer>> adjacencyList, int source, int destination, int[] visited) {
        if (source == destination)
            return true;
        visited[source] = 1;

        for (int neighbor : adjacencyList.get(source)) {
            if (visited[neighbor] == 0 && dfs(adjacencyList, neighbor, destination, visited))
                return true;
        }

        return false;
    }

    public boolean validPath(int n, int[][] edges, int source, int destination) {
        List<List<Integer>> adjacencyList = new ArrayList<>();
        int[] visited = new int[n];

        for (int i = 0; i < n; i++) {
            adjacencyList.add(new ArrayList<>());
        }

        for (int[] edge : edges) {
            int u = edge[0];
            int v = edge[1];

            adjacencyList.get(u).add(v);
            adjacencyList.get(v).add(u);
        }

        return dfs(adjacencyList, source, destination, visited);
    }
}