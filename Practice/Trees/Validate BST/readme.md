# Validate Binary Search Tree
[Link](https://leetcode.com/problems/validate-binary-search-tree/description/)

## Problem Statement

Given the root of a binary tree, determine if it is a valid binary search tree (BST).

A valid BST is defined as follows:

The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.

## Solution Explanation

We will use the Binary Search Tree basics that **left child is smaller than the root and right child is greater than the root**.

We will use ranges to determine if the current node is a valid node. We can think of an approach where we only check against the parent node but this will fail, why? 
If we check only against the parent node then we do not have the visibilty in the actual range of values a node can have. 
>Suppose root node value is 5 and left child node value is 2. Now if for left's child node we only check with left node's val i.e 2 then its right child can have any value > 2 and we may think it to be valid but clearly we cannot have any value > 2, it is limited by root node's value which is 5. So we need to maintain a range, as in this case the range for the left node's right child will be (2,5)


Initially for the left subtree the values can be present in the range (-inf,root.val)

Similarly for the right subtree the values can be present in the range (root.val, inf)

Following this as we can down the subtrees, the ranges will change accordingly for each node, based on the parent node and root node values.


