# Insert into a Binary Search tree
[Link](https://leetcode.com/problems/insert-into-a-binary-search-tree/description/)

## Problem Statement

You are given the root node of a binary search tree (BST) and a value to insert into the tree. Return the root node of the BST after the insertion. It is guaranteed that the new value does not exist in the original BST.

Notice that there may exist multiple valid ways for the insertion, as long as the tree remains a BST after insertion. You can return any of them.

## Solution Explanation

We will use the Binary Search Tree basics that **left child is smaller than the root and right child is greater than the root**.

Now we will traverse the tree checking if the current node is either greater or lesser than the given value. There is no need to check for equality as constraint is that all the node vals are unique and target is not present in the tree.
If the val is greater than the current node value, we will start checking in right child else check in left child.

Finally when we reach a null value this means we have reached the leaf node and based on the above logic we would already either be on left or right as per the requirement, thus we will add the new Treenode here.
