# Check Completeness of a Binary Tree

[Check Completeness of a Binary Tree](https://leetcode.com/problems/check-completeness-of-a-binary-tree/description/)

## Problem Statement

Given the root of a binary tree, determine if it is a complete binary tree.

In a complete binary tree, every level, except possibly the last, is completely filled, and all nodes in the last level are as far left as possible. It can have between 1 and 2h nodes inclusive at the last level h.

## Solution Explanation

Based on the complete tree logic we will maintain a flag which will track if we have encountered any node which is empty.
We will do the BFS traversal and if we find a node we first check if the flag is true or not. If the flag is true this means that current node comes after an empty node so we will return False.
In case the flag is False we will simply add the node's left and right child without checking if they exist or not. This way suppose left child is missing we will add the empty/null node to the tree.
If the node is null we will update the flag to be True.

No need of a level order solution, basic solution should suffice here.