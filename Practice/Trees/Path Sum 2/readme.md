# Path Sum II

[Path Sum II](https://leetcode.com/problems/path-sum-ii/description/)

Given the root of a binary tree and an integer targetSum, return all root-to-leaf paths where the sum of the node values in the path equals targetSum. Each path should be returned as a list of the node values, not node references.

A root-to-leaf path is a path starting from the root and ending at any leaf node. A leaf is a node with no children.

Input: root = [5,4,8,11,null,13,4,7,2,null,null,5,1], targetSum = 22
Output: [[5,4,11,2],[5,8,4,5]]

## Prac 1 thought process

---

We can see that this problem is a combo of tree + DP solution. For DP we know that we need to use backtracking to be able traverse all the nodes.
In case of tree we need to traverse both left and right child. Since a node has 2 children so when we push a node in the data structure maintaining current, we can pop it out only after both the sub trees have been traversed. => only thing to keep track of
Rest solution is same the target sum solution
