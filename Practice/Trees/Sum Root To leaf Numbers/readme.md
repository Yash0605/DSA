# Sum Root to Leaf Numbers

[Sum Root to Leaf Numbers](https://leetcode.com/problems/sum-root-to-leaf-numbers/description/)

You are given the root of a binary tree containing digits from 0 to 9 only.

Each root-to-leaf path in the tree represents a number.

For example, the root-to-leaf path 1 -> 2 -> 3 represents the number 123.
Return the total sum of all root-to-leaf numbers. Test cases are generated so that the answer will fit in a 32-bit integer.

A leaf node is a node with no children.

## Prac 1 thought process

---

We can see that this problem is a combo of tree + DP solution. For DP we know that we need to use backtracking to be able traverse all the nodes.
In case of tree we need to traverse both left and right child. Since a node has 2 children so when we push a node in the data structure maintaining current, we can pop it out only after both the sub trees have been traversed. => only thing to keep track of
Rest solution is same the target sum solution
