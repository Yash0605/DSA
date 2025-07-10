# Shortest Path in Binary Matrix

[Shortest Path in Binary Matrix](https://leetcode.com/problems/shortest-path-in-binary-matrix/description/)

## Problem Statement

Given an n x n binary matrix grid, return the length of the shortest clear path in the matrix. If there is no clear path, return -1.

A clear path in a binary matrix is a path from the top-left cell (i.e., (0, 0)) to the bottom-right cell (i.e., (n - 1, n - 1)) such that:

All the visited cells of the path are 0.
All the adjacent cells of the path are 8-directionally connected (i.e., they are different and they share an edge or a corner).
The length of a clear path is the number of visited cells of this path.

## Solution Explanation

First impression is to use DFS and then use some memoization to get the min value but it is not recommended for this problem. Here's why:

🔥 Why DFS is a poor choice here:
The problem asks for the shortest path — DFS explores deep before wide, which means it can explore long, inefficient paths before ever considering the shortest one.

DFS may visit the same cell multiple times with longer paths unless you carefully track the shortest distance to each cell.

It's hard to prune worse paths without memoization or extra logic, making it slower and more memory-intensive.

In worst-case scenarios (e.g., large open grids), DFS could be exponentially slower than BFS.
