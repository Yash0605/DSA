# Rotting Oranges

[Rotting Oranges](https://leetcode.com/problems/rotting-oranges/description/)

## Problem Statement

You are given an m x n grid where each cell can have one of three values:

0 representing an empty cell,
1 representing a fresh orange, or
2 representing a rotten orange.
Every minute, any fresh orange that is 4-directionally adjacent to a rotten orange becomes rotten.

Return the minimum number of minutes that must elapse until no cell has a fresh orange. If this is impossible, return -1.

## Solution Explanation

We need to increment time by a minute whenever any fresh orange that is 4-directionally adjacent to a rotten orange so we need to know at each min which oranges have become rotten.
If we think this is similar to level order traversal where each level will be traversed togethere.
So we need to use a BFS level order approach where we start with list of rotten oranges and at each level increment the time and check if any fresh oranges are remaining and continue till either all the oranges are rotten or no more fresh oranges can be reached. 
