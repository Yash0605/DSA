# Populating Next Right Pointers in Each Node II

[Populating Next Right Pointers in Each Node II](https://leetcode.com/problems/populating-next-right-pointers-in-each-node-ii/description/)

## Problem Statement

Given a binary tree

struct Node {
int val;
Node *left;
Node *right;
Node \*next;
}
Populate each next pointer to point to its next right node. If there is no next right node, the next pointer should be set to NULL.

Initially, all next pointers are set to NULL.

## Solution Explanation

Same as solution for part 1 only difference is that there we had a perfect binary tree so we were able to point to some of the nodes directly. Here we need a more generalized approach. Solution wise implementing this is easier.
Basic logic of using level order traversla is same. We need to see how level order traversal will work in case of nodes => instead of list we maintain a dummy Node and a tail node which would help to traverse the current level.
