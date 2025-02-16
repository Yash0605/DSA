# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        # need to get the nodes at the last level
        q = deque()
        q.append(root)

        while len(q)>0:
            current_length = len(q)
            temp = []
            for i in range(current_length):
                current_node = q.popleft()

                temp.append(current_node.val)

                if current_node.left:
                    q.append(current_node.left)
                if current_node.right:
                    q.append(current_node.right)

            final_sum = sum(temp)

        return final_sum