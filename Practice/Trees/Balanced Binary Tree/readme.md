# Balanced Binary Tree

[Balanced Binary Tree](https://leetcode.com/problems/balanced-binary-tree/description/)

Given a binary tree, determine if it is height-balanced.
A height-balanced binary tree is a binary tree in which the depth of the two subtrees of every node never differs by more than one.

## Prac 1 thought process

We know how to find the height for each node. Using DP we can check for each left and right child what is the height. If we see that the height diff is greater than 1 then we return -1.
Now using this as a flag we can know whether a subtree is balanced or not and directly return -1 for an unbalanced tree.
