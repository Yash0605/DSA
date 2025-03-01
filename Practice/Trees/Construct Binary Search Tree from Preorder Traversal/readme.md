# Construct Binary Search Tree from Preorder Traversal

[Problem Link](https://leetcode.com/problems/construct-binary-search-tree-from-preorder-traversal/description/)

`Prac 1 thought process`
------------------------------

In case of trees we needed 2 Traversals to determine the tree but in case of BST we can do it with a Preorder Traversal. This is because in BST we know that left child < root < right child value. So with preorder traversal we know that the first value will be the root. By traversing through the preorder traversal we can detemine nodes for left and right subtree. Any node greater than root will belong to right subtree. Recursively we can get the trees following this.
