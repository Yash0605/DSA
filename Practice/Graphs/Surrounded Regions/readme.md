# Surrounded Regions

[Surrounded Regions](https://leetcode.com/problems/surrounded-regions/description/)

## Problem Statement

You are given an m x n matrix board containing letters 'X' and 'O', capture regions that are surrounded:

Connect: A cell is connected to adjacent cells horizontally or vertically.
Region: To form a region connect every 'O' cell.
Surround: The region is surrounded with 'X' cells if you can connect the region with 'X' cells and none of the region cells are on the edge of the board.
To capture a surrounded region, replace all 'O's with 'X's in-place within the original board. You do not need to return anything.

## Solution Explanation

The solution is same as number of closed islands => we remove the flood fill cells i.e border cells which has 'O' or cells which are connected to border cells having 'O' needs to be excluded which is left as is.
So in first pass we need to mark these cells => we can mark with any letter other than X and O Eg:T

In second pass whichever cells are still O we can safely assume these are surrounded required surrounded regions and we can mark them as X
At the same time we can change back the cells marked as T to O

`Some considerations`:
We can use a visited matrix but that increases the Space complexity => better to use an in place update of O cells
We can traverse the border cells and its connected cells using a grid traversal => m\*n but this leads to the same problem that we would unnecessarly check for cells which we know will not give us the result i.e if we have 10 doors and we know only 2 will open so no point in checking other 8 to see if these open or not => Increases Time complexity for this traversal
Even though overall TC remains same but this will reduce performance
