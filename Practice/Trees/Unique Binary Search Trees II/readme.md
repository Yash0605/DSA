# Unique Binary Search Trees II

[Unique Binary Search Trees II](https://leetcode.com/problems/unique-binary-search-trees-ii/description/)

## Problem Statement

Given an integer n, return all the structurally unique BST's (binary search trees), which has exactly n nodes of unique values from 1 to n. Return the answer in any order.

## Solution Explanation

We know BST has the logic Left < Root < Right. Based on this we can generate the trees. From the problem we see that we need to consider all the n values as root once and generate possible trees.
For each n value as root => we know it will have left and right nodes => These nodes can itself be trees.
So we will traverse the n values keeping each as root and generate possible left an right subtrees.
Finally we will traverse the left and right generated sub trees and attach to the root.
Eg: n = 6 and current i = 3
=> left = [1,2] and right = [4,5,6]
When we say left is [1,2] we don't simply mean the values which are lesser than i but these are roots of the trees which can be possible on the left and right side.
This way we will get all the subtrees and on traversal we will get the complete tree with

```python
                for l in left: # will have subtrees where 1 is th root and then 2 is the root=> so with  1 as left we explore all the possible right subtrees and then with 2.
                    for r in right:
                        root = TreeNode(i)
                        root.left = l
                        root.right = r
                        ans.append(root)
```
