# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        """
        Optimizing for both time and space
        """
        seen_nodes = set()

        def traverse(root):
            if not root:
                return False

            check_value = k - root.val
            if check_value in seen_nodes:
                return True
            seen_nodes.add(root.val)

            return traverse(root.left) or traverse(root.right)

        return traverse(root)
