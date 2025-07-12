# Construct Binary Tree from Inorder and Postorder Traversal

[Construct Binary Tree from Inorder and Postorder Traversal](https://leetcode.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal/description/)

## Problem Statement

Given two integer arrays inorder and postorder where inorder is the inorder traversal of a binary tree and postorder is the postorder traversal of the same tree, construct and return the binary tree.

## Solution Explanation

From the inorder we can determine the left and right children if we know the index of the root. From the postorder we know root will be the last element always. So using this we find the index of the root in inorder list and based on this get the length of left children.
Using these values we can determine the left and right subtree for the root and recursively find the tree for left and right sub tree.
Base case would be the variables for end Index should not be lesser than the varaibles for start index.
