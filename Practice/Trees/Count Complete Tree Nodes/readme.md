# Count Complete Tree Nodes

[Count Complete Tree Nodes](https://leetcode.com/problems/count-complete-tree-nodes/description/)

Given the root of a complete binary tree, return the number of the nodes in the tree.

According to Wikipedia, every level, except possibly the last, is completely filled in a complete binary tree, and all nodes in the last level are as far left as possible. It can have between 1 and 2h nodes inclusive at the last level h.

Design an algorithm that runs in less than O(n) time complexity.

## Prac 1 thought process

---

Complete Binary Tree: A binary tree where all levels are fully filled except possibly the last, which is filled from left to right.
We can use basic BFS or DFS traversal to get the ans in O(n) time. the logic becomes tricky when we try to implement the sol in less than O(n) time.
We can use the uses properties of complete trees to count in O(log² n) time.
There can either be some missing nodes on the right subtree or extra node in left subtree if the tree is not perfect binary tree.
So we have 2 cases:
=> Case 1 where height of left sub tree is equal to right subtree
=> so left subtree is perfect and we can find the num nodes using pow(2^left_height)-1
=> now either right can be perfect or not => so we need to count the nodes in right subtree
=> Case 2 where left <> right subtree => left height will be right_height+1 as we are given complete binary tree
=> Now in this case we can be sure that the right is perfect tree as this the property of given complete tree => so the num nodes using pow(2^right_height)-1
=> we can find the num nodes in left by recursively using the same count nodes function.

⚡ Time Complexity
In a complete binary tree:

getDepth runs in O(log n)

At most log n recursive calls

So, overall time: O(log² n)
