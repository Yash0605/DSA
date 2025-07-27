# Binary Search Tree Iterator

[Binary Search Tree Iterator](https://leetcode.com/problems/binary-search-tree-iterator/description/)

## Problem Statement

Implement the BSTIterator class that represents an iterator over the in-order traversal of a binary search tree (BST):

BSTIterator(TreeNode root) Initializes an object of the BSTIterator class. The root of the BST is given as part of the constructor. The pointer should be initialized to a non-existent number smaller than any element in the BST.
boolean hasNext() Returns true if there exists a number in the traversal to the right of the pointer, otherwise returns false.
int next() Moves the pointer to the right, then returns the number at the pointer.
Notice that by initializing the pointer to a non-existent smallest number, the first call to next() will return the smallest element in the BST.

You may assume that next() calls will always be valid. That is, there will be at least a next number in the in-order traversal when next() is called.

## Solution Explanation

One way to solve it is havign a list where we store the inorder traversal and then use this list to perform the next and has next ops
    => This way time complexity will be O(1) for both the ops
    => But space complexity would be O(N)

We can improve upon the space => rather than storing entire tree we can simulate the in-order traversal using a controlled recursion with a stack, only storing up to height of tree nodes at a time
We know that inorder traversal is in sorted for BST and we have the order Left, Root and Right.
=> So what we can do si initially store the root to left most child nodes in the initial stack.
=> Whenever we need a next element we pop from the stack and check if it has right child
    => if so we add it with its left children => this way we always get the smallest elem => sorted
    => We don't have to store the entire tree rather only O(H) nodes.
