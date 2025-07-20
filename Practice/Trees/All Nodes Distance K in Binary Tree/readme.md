# All Nodes Distance K in Binary Tree

[All Nodes Distance K in Binary Tree](https://leetcode.com/problems/all-nodes-distance-k-in-binary-tree/description/)

## Problem Statement

Given the root of a binary tree, the value of a target node target, and an integer k, return an array of the values of all nodes that have a distance k from the target node.

You can return the answer in any order.

## Solution Explanation

We have the child details for each node so from target we can find which children are at distance K. The problem arises when we want to check for the nodes in the path above our target i.e connected via parent. In tree implementation we do not have the reference of the parent from the child.
So for this we need to create a map from parent to child and using this we can traverse to get all the nodes at distance k. We need to maintain a visited set so that we dont traverse a node again and again
We can either create the map using BFS or DFS
Using DFS we avoid using extra space for queue used in BFS

```python
def buildParentMap(node, parent):
    if node:
        parentMap[node] = parent
        buildParentMap(node.left, node)
        buildParentMap(node.right, node)
```
