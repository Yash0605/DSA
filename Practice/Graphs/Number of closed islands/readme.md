# Number of Closed Islands

[Number of Closed Islands](https://leetcode.com/problems/number-of-closed-islands/description/)

## Problem Statement

Given a 2D grid consists of 0s (land) and 1s (water). An island is a maximal 4-directionally connected group of 0s and a closed island is an island totally (all left, top, right, bottom) surrounded by 1s.

Return the number of closed islands.

Input: grid = [[1,1,1,1,1,1,1,0],[1,0,0,0,0,1,1,0],[1,0,1,0,1,1,1,0],[1,0,0,0,0,1,0,1],[1,1,1,1,1,1,1,0]]
Output: 2
Explanation: Islands in gray are closed because they are completely surrounded by water (group of 1s).

## Solution Explanation

Initially tried ti find a common logic where I can check which cells will form a closed island but it is difficult to track whixh cells can be considered for this one so it is easier to `remove the flood cells` first and then simply check for remaining cells.
The logic is simple but tricky to get on own. We need to find all the closed islands so we will have to not consider all the cells which have the value 0 and which are at the borders and the cells which are linked to these cells.
So what we can do is run a dfs to find all such cells and mark them as visited. Now by default all the 0 value cells which are left will form a closed island so we can do a simple dfs to count these cells.
