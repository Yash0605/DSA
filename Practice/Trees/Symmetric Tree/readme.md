# Symmetric Tree

[Symmetric Tree](https://leetcode.com/problems/symmetric-tree/description/)

Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).

## Prac 1 thought process

We need to find that left subtree and right subtree are mirror image of each other. We need to check all the cases a simple left == right check will not work. Check for None/ null cases and then need to check if root val's are equal + the left child and right child are equal or not.
