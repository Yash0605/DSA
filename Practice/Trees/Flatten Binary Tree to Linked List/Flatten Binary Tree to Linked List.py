# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def flatten(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: None Do not return anything, modify root in-place instead.
        """
        if not root:
            return None

        if root and not root.left and not root.right:
            return root

        self.prev = None

        # need to use reverse pre order traversal
        def dfs(root):
            if not root:
                return None

            dfs(root.right)
            dfs(root.left)

            root.right = self.prev
            root.left = None
            self.prev = root

        dfs(root)


# Time Complexity: O(n) where n is the number of nodes in the tree
# Space Complexity: O(h) where h is the height of the tree due to recursion stack
