# Binary Tree Maximum Path Sum

[Binary Tree Maximum Path Sum](https://leetcode.com/problems/binary-tree-maximum-path-sum/description/)

A path in a binary tree is a sequence of nodes where each pair of adjacent nodes in the sequence has an edge connecting them. A node can only appear in the sequence at most once. Note that the path does not need to pass through the root.

The path sum of a path is the sum of the node's values in the path.

Given the root of a binary tree, return the maximum path sum of any non-empty path.

## Prac 1 thought process

---

We need to find the path with max sum. For a node the path can go either go via left or right.
So `root.val+max(left,right)`
We need the max sum, so we will not consider the child which gives negative value => This ensures you're `only adding non-negative contributions` to the current node's value when computing the max path
`left = max(dfs(root.left), 0)`
