# Construct Binary Tree from Preorder and Inorder Traversal

[Construct Binary Tree from Preorder and Inorder Traversal](https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/description/)

Given two integer arrays preorder and inorder where preorder is the preorder traversal of a binary tree and inorder is the inorder traversal of the same tree, construct and return the binary tree.

## Prac 1 thought process

---

From preorder we find where is the root of the tree. Based on this we determine which is the left and right children for the root.
Missed to add the base case => remember
Failed to get the correct value of root in each recursion => keep track of how we are getting root for each call
