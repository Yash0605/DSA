# Binary Tree Preorder Traversal
[Link](https://leetcode.com/problems/binary-tree-preorder-traversal/description/)

## Problem Statement

Given the root of a binary tree, return the preorder traversal of its nodes' values.

## Solution Explanation

We will use a stack approach, it follows LIFO. For Preorder we have Root, Left, Right Traversal. In this sol we only need to see the order in which each node is traversed.
We will traverse and push right node first in stack, this way left node will always be last on the stack hence it will be popped first.
We can use both List and deque approach to implement stack in python

`Summary`

>For pure stack operations (LIFO):
A list is perfectly fine and is a little more straightforward.

>For more general double-ended operations, or if you want guaranteed 
𝑂(1) performance from both ends:
A deque is the better choice.


## Time Complexity: O(n)

## Space Complexity: O(n) - Since stack being used