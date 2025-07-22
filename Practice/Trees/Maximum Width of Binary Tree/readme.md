# Maximum Width of Binary Tree

[Maximum Width of Binary Tree](https://leetcode.com/problems/maximum-width-of-binary-tree/description/Given the root of a binary tree, return the maximum width of the given tree.

The maximum width of a tree is the maximum width among all levels.

The width of one level is defined as the length between the end-nodes (the leftmost and rightmost non-null nodes), where the null nodes between the end-nodes that would be present in a complete binary tree extending down to that level are also counted into the length calculation.

It is guaranteed that the answer will in the range of a 32-bit signed integer.

## Solution Explanation

If we consider o based index then if root has an index i then left child will be at 2*i+1 and right child at 2*i+2. Using this with level order traversal we can get the max width at each level.

For case of large i/ps teh tree can grow too large. To avoid this:

👉 Offset node indices at each level:

first_index = queue[0][1] or i == 0 for each level
Then subtract first_index from all indices at the current level. This keeps values small and avoids unnecessary growth in the virtual index space.
