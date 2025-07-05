# All Paths From Source to Target

[All Paths From Source to Target](https://leetcode.com/problems/all-paths-from-source-to-target/description/)

Given a directed acyclic graph (DAG) of n nodes labeled from 0 to n - 1, find all possible paths from node 0 to node n - 1 and return them in any order.

The graph is given as follows: graph[i] is a list of all nodes you can visit from node i (i.e., there is a directed edge from node i to node graph[i][j]).

## Prac 1 thought process

---

We have the adjacency list and we know the destination node. So we can simply traverse the neighbors of source node till we reach the destination node or the traversal ends.
I was not sure whether to use visited node or not but on solving I found out that visted is not needed as we need to find all the paths and a node can belong to 2 different paths.
As long as one of the nodes is different in the path we should be good for the case of visited list.