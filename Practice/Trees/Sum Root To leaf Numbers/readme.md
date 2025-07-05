# Sum Root to Leaf Numbers

[Sum Root to Leaf Numbers](https://leetcode.com/problems/sum-root-to-leaf-numbers/description/)

You are given the root of a binary tree containing digits from 0 to 9 only.

Each root-to-leaf path in the tree represents a number.

For example, the root-to-leaf path 1 -> 2 -> 3 represents the number 123.
Return the total sum of all root-to-leaf numbers. Test cases are generated so that the answer will fit in a 32-bit integer.

A leaf node is a node with no children.

## Prac 1 thought process

---

We need to traverse a path till we reach the leaf node. At each node we will add the val to current path val => `current=current*10 + root.val`
Once leaf node reached we will have the required value for the path, thus add it to the final ans
