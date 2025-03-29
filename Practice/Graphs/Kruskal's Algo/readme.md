# Kruskal's Algo
[Kruskal's Algo](https://www.geeksforgeeks.org/problems/minimum-spanning-tree/1

## Problem Statement

Given a weighted, undirected, and connected graph with V vertices and E edges, your task is to find the sum of the weights of the edges in the Minimum Spanning Tree (MST) of the graph. The graph is represented by an adjacency list, where each element adj[i] is a vector containing vector of integers. Each vector represents an edge, with the first integer denoting the endpoint of the edge and the second integer denoting the weight of the edge.

## Solution Explanation

**Kruskal's Algo**:

Spanning Tree is the data structure which is formed when all the nodes of the graph is connected via edge and there are no cycles formed.
MST is the spanning tree where the edges with min wts are used to form the tree.

**Kruskal’s algorithm** is a **greedy algorithm** used to find the Minimum Spanning Tree (MST) of a connected, weighted, and undirected graph. The MST is a subset of edges that connects all vertices with the minimum total edge weight and no cycles.

Initially we will sort the edges as we want to start with the edge that has the minimum weight. Once we have the sorted edges we will traverse all the edges.
We will make use of **Disjoint Sets** to avoid cycles. Initially we will create all the nodes as their own sets. Once we start traversing we will use **FindParent** to check if the 2 nodes are already part of the same set. If they are not part of same set we will try to merge sets via **Union**.
