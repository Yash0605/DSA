# Clone Graph

[Clone Graph](https://leetcode.com/problems/clone-graph/description/)

## Problem Statement

Given a reference of a node in a connected undirected graph.

Return a deep copy (clone) of the graph.

Each node in the graph contains a value (int) and a list (List[Node]) of its neighbors.

class Node {
public int val;
public List<Node> neighbors;
}

Test case format:

For simplicity, each node's value is the same as the node's index (1-indexed). For example, the first node with val == 1, the second node with val == 2, and so on. The graph is represented in the test case using an adjacency list.

An adjacency list is a collection of unordered lists used to represent a finite graph. Each list describes the set of neighbors of a node in the graph.

The given node will always be the first node with val = 1. You must return the copy of the given node as a reference to the cloned graph.

## Solution Explanation

This will be basic DFS traversal where for each node we will need to create a new node and then recurse to create all the neighbor nodes and thelink them togethere.

The only problem here is **how to keep track of visited nodes**.

> For this we can **maintain a hashmap/ dictionary** which will store the given node as key and newly cloned node as the value. Now when we reach a neighbor we can check if the neighbor has already been cloned or not. We will have following 2 cases.

1)**If the neighbor has not been cloned**, we will call the recursive function which we will clone the node and its neighbor and link the cloned neighbor to the cloned node.

2)**If the neighbor has been cloned**, we only need to link the cloned neighbor node to the newly cloned node.

`Prac 2`:

was able to come up with the DFS logic and hashmap to store the mapping so that we can kepp track of visited nodes but used node.val as key instead of the node => need to consider the node in case the values are not unique.
