# Number of Islands

[Number of Islands](https://leetcode.com/problems/number-of-islands/description/)

## Problem Statement

Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.

An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

Example 1:

Input: grid = [
["1","1","1","1","0"],
["1","1","0","1","0"],
["1","1","0","0","0"],
["0","0","0","0","0"]
]
Output: 1

Return the total number of provinces.

## Solution Explanation

Similar to number of provinces but in this case we do not have an adjacency matrix or list instead we have the grid. We can do DFS traversal of grid, the only thing that changes is how we traverse the neighbours. For > **each cell in the grid it can be connected to 4 other cells**. [(i-1,j),(i, j+1),(i+1,j),(i,j-1)]. We need travrese as per this **delta direction logic**

Prac2:

Check the input is string and not number so compare for cell values accordingly.
