# Find Bottom Left Tree Value

[Find Bottom Left Tree Value](https://leetcode.com/problems/find-bottom-left-tree-value/description/)

## Problem Statement

Given the root of a binary tree, return the leftmost value in the last row of the tree.

## Solution Explanation

At first we can think of a Level Order Traversal where for each level we run a for loop from 0 to num nodes at that level. The left most val will be the node at i = 0.

But, We can do this w/o the inner for loop as well. We can push the right most child first and then the left child. This way when we pop from left, at the end of our iteration we will always get the left most node.
The reason behind this order is tied to the goal of the algorithm: to find the leftmost value at the last level.
By enqueueing the right child before the left child, we ensure that nodes at the same level are processed from left to right during the level-order traversal.
This guarantees that the leftmost value at the last level is encountered first, aligning with the goal of the algorithm.

## Time Complexity: O(n)

## Space Complexity: O(n)

`Prac 2`:

Knew the logic to traverse right then left but again missed that we dont really need to go level wise. We can simply do BFS and because of the right left logic we will get the left most node in the end.
