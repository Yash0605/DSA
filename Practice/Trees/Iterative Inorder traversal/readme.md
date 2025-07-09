# Binary Tree Inorder Traversal

[Binary Tree Inorder Traversal](https://leetcode.com/problems/binary-tree-inorder-traversal/description/)

Given the root of a binary tree, return the inorder traversal of its nodes' values.

## Prac 1 thought process

---

In this case we do not need 2 stacks. We have to traverse the left child first then the root and then the right child.
We cannot directly push in the root. So we maintain it in a variable current and maintain a stack to track the path.
We traverse to the left most child based on current and keep adding it to the stack and updating the current.
Once we have reached to the left most node we pop and add it to the answer => so `Left` is added
Its `parent now becomes the top of the stack` and we push its right child to the stack.
=> Case 1 if current was root the we reach the left child which is a leaf and update current with its right child i.e null in this case. So in next traversal there is no left child and when we pop we get the parent of the left and add to the answer=> `Root is now added` and then its right is set as current
=> Case 2 as above we have traversed Left and Root and the current is Right => we again get the left most node of the right child => pop and add to the answer
=> If no left child we have Right as top so we get the `Right chils as well`
