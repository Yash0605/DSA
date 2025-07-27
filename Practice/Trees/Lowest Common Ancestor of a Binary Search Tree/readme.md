# Lowest Common Ancestor of a Binary Search Tree

[Lowest Common Ancestor of a Binary Search Tree](https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/description/)

## Problem Statement

Given a binary search tree (BST), find the lowest common ancestor (LCA) node of two given nodes in the BST.

According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”

## Solution Explanation

We will use the Binary Search Tree basics that **left child is smaller than the root and right child is greater than the root**.

Following this we can have these cases:

1. Given nodes can both be on the left subtree => Traverse the Left sub tree till both the nodes are in diff sub trees => then return this node

2. Given nodes can both be on the right subtree => Traverse the Right sub tree till both the nodes are in diff sub trees => then return this node

3. One of the given nodes is the ancestor of another => Return the ancestor node

4. Both nodes are in diff sub trees => return the root node.

## `Prac2`

Knew both the solutions i.e for the LCA in Binary tree and LCA in BST. BST is easier we just need to check based on the vals which subtrees the node will be part of.
Iterative solution may be better if space is a concern => need to remember this as well might help in interviews!
