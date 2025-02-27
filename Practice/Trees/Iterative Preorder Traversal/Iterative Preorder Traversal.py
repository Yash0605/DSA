# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque


class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # using Iteartive approach
        if not root:
            return []

        q = deque([root])
        ans = []

        while len(q) > 0:
            current_node = q.pop()
            ans.append(current_node.val)

            # pushing right first as it needs to be traversed after left
            if current_node.right:
                q.append(current_node.right)

            # pushing left last as stack is LIFO and we will make use of this one to get the traversal
            if current_node.left:
                q.append(current_node.left)

        return ans
