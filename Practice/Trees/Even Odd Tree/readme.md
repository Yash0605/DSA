# Even Odd Tree

[Even Odd Tree](https://leetcode.com/problems/even-odd-tree/description/)

## Problem Statement

A binary tree is named Even-Odd if it meets the following conditions:

The root of the binary tree is at level index 0, its children are at level index 1, their children are at level index 2, etc.
For every even-indexed level, all nodes at the level have odd integer values in strictly increasing order (from left to right).
For every odd-indexed level, all nodes at the level have even integer values in strictly decreasing order (from left to right).
Given the root of a binary tree, return true if the binary tree is Even-Odd, otherwise return false.

## Solution Explanation

Basic BFS level order traversal with added logic to check for even and odd conditions as mentioned in the problem.
No need to maintain all the values at a level, we can simply maintain the last seen value.
We need to maintain the current level explicitly
