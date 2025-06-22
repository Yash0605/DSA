# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def helper(self, root, diameter):
        if not root:
            return 0

        left = self.helper(root.left, diameter)
        right = self.helper(root.right, diameter)

        diameter[0] = max(diameter[0], left + right)

        return 1 + max(left, right)

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        """
        Basic finding the depth solution might have worked
            => in this case we would have found the depth of left subtree and the depth of right subtree
            => Added the 2 values to get the final result
        But this would fail in the case where the max diameter does not go via root
            => In this case it would give the ans via root which would be incorrect
            => So we need to maintain a maxDiameter variable which keeps track of diameter of all the nodes
            => This could be checked along with calc the depth of the tree => So same TC
        """
        diameter = [0]
        self.helper(root, diameter)

        return diameter[0]
# Time Complexity: O(n) where n is the number of nodes in the tree
# Space Complexity: O(h) where h is the height of the tree due to recursion stack