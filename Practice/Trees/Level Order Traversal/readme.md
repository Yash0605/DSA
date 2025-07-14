# Level Order Traversal

[Problem Link](https://leetcode.com/problems/binary-tree-level-order-traversal/)

## `Prac 1 thought process`

Initially had thought that we need to store levels for nodes to be able to add in the final ans list. But that the ans in dictionary and then again traversing it to get the final ans.

Correct process to get the ans in format of the levels i.e if
root = [3,9,20,null,null,15,7]
Output [[3],[9,20],[15,7]]

For this in the while loop we need to maintain a **size variable**, based on this size variable we run a for loop. This will ensure that we only traverse nodes at each level rather than traversing all the nodes.

## `Prac 2`

Had missed how to get the nodes at each level => missed the concept of inner loop
`We need 2 loops` => outer while for general traversal and inner for loop to traverse the nodes at a lmevel
TC => O(N) coz the for loop also runs only once for each node
