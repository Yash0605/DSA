# Search in a Binary Search Tree

[Search in a Binary Search Tree](https://leetcode.com/problems/search-in-a-binary-search-tree/description/)

## Problem Statement

You are given the root of a binary search tree (BST) and an integer val.

Find the node in the BST that the node's value equals val and return the subtree rooted with that node. If such a node does not exist, return null.

## Solution Explanation

Basic DFS use the BST logic => left child < root < right child. If root.val == val we return the root else None
Can use iterative sol as well if issues with recursive depth
