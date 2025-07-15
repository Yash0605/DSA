# Vertical Order Traversal of a Binary Tree

[Link](https://leetcode.com/problems/vertical-order-traversal-of-a-binary-tree/description/)

## Problem Statement

Given the root of a binary tree, calculate the vertical order traversal of the binary tree.

For each node at position (row, col), its left and right children will be at positions (row + 1, col - 1) and (row + 1, col + 1) respectively. The root of the tree is at (0, 0).

The vertical order traversal of a binary tree is a list of top-to-bottom orderings for each column index starting from the leftmost column and ending on the rightmost column. There may be multiple nodes in the same row and same column. In such a case, sort these nodes by their values.

Return the vertical order traversal of the binary tree.

## Solution Explanation

Basic solution revolves around Level order traversal. The only thing we need to take care is tracking the horizontal distance and vertical distance along with push the nodes in the Queue.
In order to get the ans while traversing we need to maintain a seperate data structure which will hold the horizontal order and the vertical order + node val. As per the problem we need to sort based on the horizontal order and if required then on the vertical order.
In python can use sort or sorted. If we use sort then it will only work on list so need conversion overhead.
So sorted is the best option, it performs most of the operation in C so might be slightly better but overall worst case complexity is same for both.
Practically: sorted() is often slightly faster because it does the conversion and sorting in one highly optimized C-level operation, whereas the two-step approach incurs additional Python-level overhead.
Timsort (which both sorted() and list.sort() use) takes advantage of existing order (runs) in the data. Sometimes the keys view may already be nearly sorted, and the sorted() call can take advantage of that. When you explicitly convert to a list first, you may lose some of that benefit if you’re not careful (although in most cases it would still work similarly).

## Time Complexity: O(n log n)

## Space Complexity: O(n)

`Prac 2`:
Knew the logic to be used => missed if keys are sorted in defaultdict => these are not sorted so we need to sort them explicitly
then sort the values as well => no need to sort only on the verticla order as we can have the case where 2 nodes have the same vertical order then we need to sort based on the node values
