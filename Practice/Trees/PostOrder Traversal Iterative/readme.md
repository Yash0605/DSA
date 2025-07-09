# Binary Tree Postorder Traversal

[Binary Tree Postorder Traversal](https://leetcode.com/problems/binary-tree-postorder-traversal/description/)

## Problem Statement

Given the root of a binary tree, return the postorder traversal of its nodes' values.

## Solution Explanation

We need to maintain 2 stacks => one to traverse all the nodes and its children and other one to track the path.
Initially we push the root in main Stack
=> since we need to push the children so in order to determine we compare the head of main stack with the path stack
=> if both are same then it means we have traversed the children so we add to the answer and pop from stacks
=> else we meed to traverse the children so first add to path stack so that we can come back to it after traversal. Then add the right child followed by left as this is a stack so LIFO
