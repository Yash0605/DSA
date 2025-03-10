# 01 Matrix
[01 Matrix](https://leetcode.com/problems/01-matrix/description/)

## Problem Statement

Given an m x n binary matrix mat, return the distance of the nearest 0 for each cell.

The distance between two cells sharing a common edge is 1.

## Solution Explanation

We have 2 ways to solve this problem.

1) DP approach => For a cell having 1 the nearest 0 can either on top of it or in the bottom half of it. Based on from where we start to count the distance we will get different answer. So for this case we need to **find the nearest from both top left cell i.e 0,0 and bottom right cell i.e n-1,m-1**. Then we need to get the **min of these 2 values**. We can use the same matrix here, in order to solve this way we can update each cell with 1 value with the max value a cell can hold. In this case it will be m+n, considering all cells are 1 except for n-1,m-1 cell. So the nearest value for cell 0,0 will be n+m.
In first traversal we will update the values. In second traversal we will update the distance starting from top left. We need to consider the edge cases where n>0 ans m>0.
Then finally we will traverse from bottom right and **consider the edge cases**.

2) Graphs => Using **BFS traversal**. Again in this case we will initially update all the cells with value 1 to it max value. Now for traversal we need a source and destination. In this case cell with 0 is the source and the cell with val>0 is it destination. So we will push all the cells with value 0 in the queue. Each cell can have 4 neighbors. We need to use the delta directions solution to traverse the 4 neighbors of each cell. If the neighbor has value>0 then we can check to see if we can get a smaller value if we reach the neighbor from the current cell. If this is the case we will update the neighbor's val with the new val. We also need to put the cells in the queue after the update as these cells can have neighbors with vals>0 so this way we will get the nearest values.
