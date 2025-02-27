# Binary Tree Right Side View
[Link](https://leetcode.com/problems/binary-tree-right-side-view/)

## Problem Statement

Given the root of a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.

## Solution Explanation

Right side view is returning the right most node at each level. For this we will perform level order traversal as it is. The only thing we need is to maintain a temp variable at each level which will hold the current node being processed. So once the traversal of a level is complete we will have the last ele in temp variable and as per the logic it will be the right most node at that level.


## Time Complexity: O(n)

## Space Complexity: O(n)