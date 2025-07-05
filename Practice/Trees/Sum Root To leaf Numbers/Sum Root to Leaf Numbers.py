# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sumNumbers(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        ans = [0]

        def dfs(root, current):
            if not root:
                return

            current = current * 10 + root.val
            if not root.left and not root.right:
                ans[0] = ans[0] + current
            else:
                dfs(root.left, current)
                dfs(root.right, current)

        dfs(root, 0)
        return ans[0]


# Time Complexity: O(n) where n is the number of nodes in the tree.
# Space Complexity: O(h) where h is the height of the tree due to recursion stack
