# Diameter of Binary Tree

[Diameter of Binary Tree](https://leetcode.com/problems/diameter-of-binary-tree/description/)

Given the root of a binary tree, return the length of the diameter of the tree.

The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the root.

The length of a path between two nodes is represented by the number of edges between them.

## Prac 1 thought process

Basic finding the depth solution might have worked
            => in this case we would have found the depth of left subtree and the depth of right subtree
            => Added the 2 values to get the final result
            => Only works for root
        But this would fail in the case where the max diameter does not go via root
            => In this case it would give the ans via root which would be incorrect
            => So we need to maintain a maxDiameter variable which keeps track of diameter of all the nodes
            => This could be checked along with calc the depth of the tree => So same TC