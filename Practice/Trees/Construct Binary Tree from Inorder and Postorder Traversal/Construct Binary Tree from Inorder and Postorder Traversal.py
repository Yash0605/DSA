# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import defaultdict


class Solution:
    def helper(
        self, inorder, in_start, in_end, postorder, post_start, post_end, in_idx
    ):

        # base case
        if in_start > in_end or post_start > post_end:
            return None

        root = TreeNode(postorder[post_end])
        idx = in_idx[postorder[post_end]]
        nums_in_left = idx - in_start

        root.left = self.helper(
            inorder,
            in_start,
            idx-1,
            postorder,
            post_start,
            post_start + nums_in_left-1,
            in_idx,
        )
        root.right = self.helper(
            inorder,
            idx + 1,
            in_end,
            postorder,
            post_start + nums_in_left,
            post_end-1,
            in_idx,
        )

        return root

    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        # create dict for faster index retrieval
        in_idx = defaultdict(int)
        for i in range(len(inorder)):
            in_idx[inorder[i]] = i

        return self.helper(
            inorder, 0, len(inorder) - 1, postorder, 0, len(postorder) - 1, in_idx
        )
