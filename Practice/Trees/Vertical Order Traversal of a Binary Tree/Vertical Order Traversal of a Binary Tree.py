# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque, defaultdict


class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        q = deque()
        final_dict = defaultdict(list)
        ans = []

        q.append((root, 0, 0))

        while len(q) > 0:
            s = len(q)
            
            for i in range(s):
                current_node, row, col = q.popleft()
                
                final_dict[col].append((row, current_node.val))

                if current_node.left:
                    q.append((current_node.left, row+1, col-1))

                if current_node.right:
                    q.append((current_node.right, row+1, col+1))

        # keys = list(final_dict.keys())
        # keys.sort()

        for key in sorted(final_dict.keys()):
            temp = []
            val = final_dict[key]
            # val.sort()

            for row, node_value in sorted(val):
                temp.append(node_value)

            ans.append(temp[:])

        return ans