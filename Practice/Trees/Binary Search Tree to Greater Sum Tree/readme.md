# Binary Search Tree to Greater Sum Tree

[Binary Search Tree to Greater Sum Tree](https://leetcode.com/problems/binary-search-tree-to-greater-sum-tree/description/)

## Problem Statement

Given the root of a Binary Search Tree (BST), convert it to a Greater Tree such that every key of the original BST is changed to the original key plus the sum of all keys greater than the original key in BST.

As a reminder, a binary search tree is a tree that satisfies these constraints:

The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.

## Solution Explanation

We need to use reverse inorder traversal because we need to add the sum of all the nodes where value is greater than the current node.
So we start from right node => add the value to a global variable and update the root value.
Then we traverse the left node and update its root value in the same way.
