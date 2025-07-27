# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

"""
We can have following cases:
Both p and q are in left subtree - go left and check till Both are in different subtree
Both p and q are in right subtree - go right and check till Both are in different subtree
Either one is the ancestor of the other - return the ancestor node
Both are in different subtree => return root
"""


class Solution:
    def lowestCommonAncestor(
        self, root: "TreeNode", p: "TreeNode", q: "TreeNode"
    ) -> "TreeNode":
        if p.val < root.val and q.val < root.val:
            return self.lowestCommonAncestor(root.left, p, q)
        if p.val > root.val and q.val > root.val:
            return self.lowestCommonAncestor(root.right, p, q)
        return root


# Iterative solution
class Solution:
    def lowestCommonAncestor(
        self, root: "TreeNode", p: "TreeNode", q: "TreeNode"
    ) -> "TreeNode":
        while root:
            if p.val < root.val and q.val < root.val:
                root = root.left
            elif p.val > root.val and q.val > root.val:
                root = root.right
            else:
                return root
# Time Complexity: O(h) where h is the height of the tree
# Space Complexity: O(1) for iterative solution, O(h) for recursive solution due to recursion stack