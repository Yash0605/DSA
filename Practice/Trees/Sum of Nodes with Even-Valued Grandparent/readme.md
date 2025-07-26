# Sum of Nodes with Even-Valued Grandparent

[Sum of Nodes with Even-Valued Grandparent](https://leetcode.com/problems/sum-of-nodes-with-even-valued-grandparent/description/)

## Problem Statement

Given the root of a binary tree, return the sum of values of nodes with an even-valued grandparent. If there are no nodes with an even-valued grandparent, return 0.

A grandparent of a node is the parent of its parent if it exists.

## Solution Explanation

Initially looks like a BFS level order traversal problem where we keep a map of parent and then at each level check if granparent is even => add the node val to final sum. Time wise this is optimal but we will need extra space to store the parent map which is not required.

We can use a DFS solution where we pass in the node, parent and grandparent. At each step we are aware of all the 3 values so we can simply use it and then keep on adding to the final answer if the condition is satisfied. Not intutive for me as I prefer BFS over DFS but will come easily with practice.
