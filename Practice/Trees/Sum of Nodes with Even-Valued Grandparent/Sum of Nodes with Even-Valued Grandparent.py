# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sumEvenGrandparent(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """

        def dfs(node, parent, grandParent):
            if not node:
                return 0

            answer = 0
            if grandParent and grandParent.val % 2 == 0:
                answer += node.val

            answer += dfs(node.left, node, parent)
            answer += dfs(node.right, node, parent)

            return answer

        return dfs(root, None, None)


# Time Complexity: O(n) where n is the number of nodes in the tree
# Space Complexity: O(h) where h is the height of the tree due to recursion stack
