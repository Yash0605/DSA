# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque


class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        ans = []
        q = deque([root])

        while len(q) > 0:
            s = len(q)
            temp = []
            for i in range(s):
                current_node = q.popleft()

                if current_node.left:
                    q.append(current_node.left)
                if current_node.right:
                    q.append(current_node.right)

                temp.append(current_node.val)

            if len(ans) % 2 != 0:
                temp.reverse()

            ans.append(temp[:])

        return ans


# Time Complexity: O(n)
# Space Complexity: O(n)
