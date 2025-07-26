# Two Sum IV - Input is a BST

[Two Sum IV - Input is a BST](https://leetcode.com/problems/two-sum-iv-input-is-a-bst/description/)

## Problem Statement

Given the root of a binary search tree and an integer k, return true if there exist two elements in the BST such that their sum is equal to k, or false otherwise.

## Solution Explanation

One way to solve it is getting the inorder traversal of BST which will be sorted due to its property and then using a 2 pointer approach to get the result.

It's optimal in time, but not in space.
This is using O(n) space — but this problem can be solved using O(h) space (h = height of tree)
with a more space-efficient approach. => but too complex
It is a good and acceptable sol, but can optimize space further using the set method or iterator-based two-pointer(complex).

Optimizing for both time and space:
We can keep a seen set where we check for each node if the complement exists is the set or not. If it exists we return True else keep checking all the nodes.

Even if both solutions have the same Big-O, the hashset solution is often preferred for its practical performance (early exit), simplicity, and flexibility. That's why it's commonly seen in interviews and accepted as optimal in LeetCode discussions.
