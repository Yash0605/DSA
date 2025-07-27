# Construct Binary Search Tree from Preorder Traversal

[Construct Binary Search Tree from Preorder Traversal](https://leetcode.com/problems/construct-binary-search-tree-from-preorder-traversal/description/)

Given an array of integers preorder, which represents the preorder traversal of a BST (i.e., binary search tree), construct the tree and return its root.

It is guaranteed that there is always possible to find a binary search tree with the given requirements for the given test cases.

A binary search tree is a binary tree where for every node, any descendant of Node.left has a value strictly less than Node.val, and any descendant of Node.right has a value strictly greater than Node.val.

A preorder traversal of a binary tree displays the value of the node first, then traverses Node.left, then traverses Node.right.

## `Prac 1 thought process`

In case of trees we needed 2 Traversals to determine the tree but in case of BST we can do it with a Preorder Traversal. This is because in BST we know that left child < root < right child value. So with preorder traversal we know that the first value will be the root. By traversing through the preorder traversal we can detemine nodes for left and right subtree. Any node greater than root will belong to right subtree. Recursively we can get the trees following this.

## `Prac 2`

On checking I see that the above solution suggested by keerthi will have an O(N^2) Time comlexity if the tree is skewed. Example:
preorder = [1, 2, 3, 4, 5]
Let’s walk through your solution step by step:

At each level:

You do a linear scan over the entire remaining list (to find first > root)

So at level 1: scan 4 elements
level 2: scan 3 elements
level 3: scan 2 elements
level 4: scan 1 element

(4 + 3 + 2 + 1) = O(N²) time

We can achieve the result in O(N) time. We know that left child < root < right child. So we keep a global index which will help us to traverse the preorder list.
While traversing for each element we check it against an upper bound value. If the value is greater than this upeer bound we can safely say it belongs to right subtree else it belongs to left subtree.
For left we know the upper bound will be root value while for right it is inf
