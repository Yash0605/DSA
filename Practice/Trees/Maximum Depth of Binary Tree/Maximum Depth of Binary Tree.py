# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxDepthHelper(self, root):
        if not root:
            return 0

        left = 1 + self.maxDepthHelper(root.left)
        right = 1 + self.maxDepthHelper(root.right)

        return max(left, right)

    def maxDepth(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        return self.maxDepthHelper(root)


# Time Complexity: O(n) where n is the number of nodes in the tree
# Space Complexity: O(h) where h is the height of the tree due to recursion stack
