# Maximum Level Sum of a Binary Tree

[Maximum Level Sum of a Binary Tree](https://leetcode.com/problems/maximum-level-sum-of-a-binary-tree/description/)

## Problem Statement

Given the root of a binary tree, the level of its root is 1, the level of its children is 2, and so on.

Return the smallest level x such that the sum of all the values of nodes at level x is maximal.

## Solution Explanation

Basic Level order traversal where at each level we keep track of sum and check if its greater than max sum and update the max sum and max level accordingly
