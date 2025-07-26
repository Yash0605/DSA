# Flatten Binary Tree to Linked List

[Flatten Binary Tree to Linked List](https://leetcode.com/problems/flatten-binary-tree-to-linked-list/description/)

## Problem Statement

Given the root of a binary tree, flatten the tree into a "linked list":

The "linked list" should use the same TreeNode class where the right child pointer points to the next node in the list and the left child pointer is always null.
The "linked list" should be in the same order as a pre-order traversal of the binary tree.

## Solution Explanation

We need to do a reverse pre order traversal, this we will have the right child available in dfs. We can keep a prev variable which will help us to track the current right most element.
For the last ele right will be None so we will simply assign prev as None.
Once we start traversing we will keep on updating prev with the current right child, this way we will form the required linked list starting from the end.
