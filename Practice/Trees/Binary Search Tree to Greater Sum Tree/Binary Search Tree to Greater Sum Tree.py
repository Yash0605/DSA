# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstToGst(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        self.val = 0

        def getUpdatedRoot(root):
            if root.right:
                getUpdatedRoot(root.right)

            self.val += root.val
            root.val = self.val

            if root.left:
                getUpdatedRoot(root.left)

            return root

        return getUpdatedRoot(root)


# Time Complexity: O(n) - where n is the number of nodes in the tree
# Space Complexity: O(h) - where h is the height of the tree due to recursion stack
