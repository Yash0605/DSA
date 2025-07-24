# Is Graph Bipartite?

[Is Graph Bipartite?](https://leetcode.com/problems/is-graph-bipartite/description/)

## Problem Statement

There is an undirected graph with n nodes, where each node is numbered between 0 and n - 1. You are given a 2D array graph, where graph[u] is an array of nodes that node u is adjacent to. More formally, for each v in graph[u], there is an undirected edge between node u and node v. The graph has the following properties:

There are no self-edges (graph[u] does not contain u).
There are no parallel edges (graph[u] does not contain duplicate values).
If v is in graph[u], then u is in graph[v] (the graph is undirected).
The graph may not be connected, meaning there may be two nodes u and v such that there is no path between them.
A graph is bipartite if the nodes can be partitioned into two independent sets A and B such that every edge in the graph connects a node in set A and a node in set B.

Return true if and only if it is bipartite.

## Solution Explanation

A graph is bipartite if the nodes can be partitioned into two independent sets A and B such that every edge in the graph connects a node in set A and a node in set B. Eg. if we go on to color each node with color a or b. Then every alternate node should have a different color. If the 2 nodes connected via edge has the same color then the graph is not Bipartite.
In the following example we can color 0 with Blue, 1 with Red, 2 with Blue and 3 with Red. So none of the nodes with same color are conected via edge hence Bipartite.

![Bipartite Graph](https://assets.leetcode.com/uploads/2020/10/21/bi1.jpg)

We can solve this **either via DFS or BFS**. We can create seperate data structure to keep track of visited node and colored nodes but we can also do this in the same data structure.
We can have a visitedNodes list which we can initialize with any number Eg -1 to mark them as unvisited. For marking as colored we can simply choose any 2 numbers Eg 0 and 1. This way if the visitedNodes[node] == -1 we know its unvisited.
While traversing we have 2 cases:

1)**Node has not been visited**. In this case we can mark the node with a color different than the neighbor node. i.e If neighbor node had color 1 we will color this as 2.

2)**Node has been visited**. In this case we need to check if the node has a different color than the neighbor node. i.e If neighbor node had color 1 it should have 2. If both the nodes have same color then this cannot be a bipartite graph, return False

## `Prac 2`:

Was able to come up with the logic where we can have a visitedNodes list which we can initialize with a -1 to mark them as unvisited and use 0 and 1 to toggle the logic.
Missed on the conditions of how to check the colors and when to return False. This cand be done is single pass => but was not sure while implementing if needs to be done is single pass or update the colors first and then check if bipartite or not
