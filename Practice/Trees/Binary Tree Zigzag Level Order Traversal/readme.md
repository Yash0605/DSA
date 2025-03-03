# Binary Tree Zigzag Level Order Traversal
[Binary Tree Zigzag Level Order Traversal](https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/description/)

## Problem Statement

Given the root of a binary tree, return the zigzag level order traversal of its nodes' values. (i.e., from left to right, then right to left for the next level and alternate between).

## Solution Explanation

Same sol as Level Order Traversal => only thing we need to track is the zig zag pattern in which we need to return the ans.
From the problem we can see the pattern will be reversed when there is odd number of elements in the final ans. So when the ans has odd elements we will reverse the temp list and then append to the final ans list.