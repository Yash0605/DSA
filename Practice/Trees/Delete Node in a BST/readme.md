# Delete Node in a BST
[Link](https://leetcode.com/problems/delete-node-in-a-bst/description/)

## Problem Statement

Given a root node reference of a BST and a key, delete the node with the given key in the BST. Return the root node reference (possibly updated) of the BST.

Basically, the deletion can be divided into two stages:

Search for a node to remove.
If the node is found, delete the node.

## Solution Explanation

We will use the Binary Search Tree basics that **left child is smaller than the root and right child is greater than the root**. Expanding on this we have concept of **Successor** which is the next element greater than the current node and **Predecessor** which is the prev element smaller than the current node.

Firstly we will traverse to search for the node to be deleted. Once we have found the node we will have the following cases:
The node can be a leaf node => in this case we can simply replace with null
The node has only 1 child => we will return the child
The case where it has both the children or has a subtree for the child nodes => In this case we can either replace with Successor or Predecessor.

> In case of **Successor** - we will have to replace with next biggest node => Since we need greater val we will traverse the right sub tree. On the right sub tree it will be the smallest value => so we get the left most val in this right subtree. We will replace the current node val with the Successor node val and then we **also need to delete the successor node** from the right sub tree. So we will again use the recursion with root as root.right and target as the successor value.

>In case of **Predecessor** - we will have to replace with previous smaller node => Since we need smaller val we will traverse the left sub tree. On the left sub tree it will be the largest value => so we get the right most val in this left subtree. We will replace the current node val with the Predecessor node val and then we **also need to delete the Predecessor node** from the left sub tree. So we will again use the recursion with root as root.left and target as the Predecessor value.

Things to keep track of => we will always need to assign the left and right when we do a recursion else we will not get the updated value.
