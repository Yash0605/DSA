# Populating Next Right Pointers in Each Node

[Populating Next Right Pointers in Each Node](https://leetcode.com/problems/populating-next-right-pointers-in-each-node/description/)

## Problem Statement

You are given a perfect binary tree where all leaves are on the same level, and every parent has two children. The binary tree has the following definition:

struct Node {
int val;
Node *left;
Node *right;
Node \*next;
}
Populate each next pointer to point to its next right node. If there is no next right node, the next pointer should be set to NULL.

Initially, all next pointers are set to NULL.

## Solution Explanation

Basic level order traversal where we keep track of the nodes at a level and then we can simply update the next of each node
Time wise this is optimal but this is not space optimized => In order to optimize the space we need to make use of the next pointer.
In the case of perfect binary tree we are sure that we will have left child and right might bemissing.
So whil traversing we can simply point the left next to right child.
Only problem is how we deal with pointing next of right to the left of next node. Since perfect we have all the required pointers we can directly use it.
Overall logic is same as level order traversal only we need to take care of how we traverse the nodes in a level using pointers.
