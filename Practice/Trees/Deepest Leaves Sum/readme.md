# Deepest Leaves Sum

## Problem Statement

Given the `root` of a binary tree, return the sum of values of its deepest leaves.

## Solution Explanation

### Approach

We need to traverse all the nodes level wise and consider current level to be the deepest. Finally return the sum of the last level.

### Steps

Traverse the tree level wise
At each level sum the node values
If deeper level found, update the sum with this levels value
Return the final sum

## Time Complexity: O(n)

## Space Complexity: O(n) - If temp used, can be solved without this as well so O(1)
