'''
Problem statement
Ninja and his girlfriend want to shift to a new locality and want their houses distant. The homes in that locality are like nodes of a “Binary Search Tree.”

The distance between the houses is the difference between the house numbers.

Help Ninja and his girlfriend find the required location.

So, your task is to find the minimum absolute difference between any two nodes.

Note:

A binary search tree is a binary tree data structure, with the following properties
The left subtree of any node contains nodes with a value less than the node’s value. The right subtree of any node contains nodes with a value equal to or greater than the node’s value. Right, and left subtrees are also binary search trees.

Example:

consider the following binary search tree, so the minimum absolute difference is between the node value, i.e., | 15-13 |= ‘2’so ‘2’is our answer.
'''

from os import *
from sys import *
from collections import *
from math import *

''' 
    Following is the TreeNode class structure

    class   TreeNode :
        def __init__(self, val) :
            self.val = val
            self.left = None
            self.right = None

        def __del__(self):
            if self.left:
                del self.left
            if self.right:
                del self.right

'''
def inorder(root, ans):
    if not root:
        return

    inorder(root.left, ans)
    ans.append(root.data)
    inorder(root.right, ans)

def ninjaGf(root):
    # Write your code here
    # get inorder of the bst and then calc the min diff
    min_diff = inf
    ans = []
    inorder(root, ans)

    for i in range(len(ans)-1):
        min_diff = min(min_diff, ans[i+1]- ans[i])
    return min_diff
