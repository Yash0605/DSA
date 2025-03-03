# Lowest Common Ancestor of a Binary Tree
[Lowest Common Ancestor of a Binary Tree](https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/description/)

## Problem Statement

Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.

According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”

## Solution Explanation

This is a different case than BST as in BST it is guranteed that the smaller nodes will be in Left Sub tree and Greater nodes will be in Right Sub Tree.

**In this case we will have to traverse both left and right subtree**

1) Either of p or q can be ancestor => return ancestor
2) if both present in left => traverse in left subtree till we get one in left and other in right else need to return None => Edge case in recursion func
3) if both present in right => traverse in right subtree till we get one in left and other in right else need to return None

Things to track => We need to consider the case where both left and right children return None
Need to create fun with this in mind, we cannot return root at the end of the recursive func if we are using the same func
    => or we need to expicitly mention the case where p and q not part of the subtree
