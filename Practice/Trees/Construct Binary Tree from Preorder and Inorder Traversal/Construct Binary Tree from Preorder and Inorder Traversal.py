# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def get_root_index(self, inorder, val):
        for i in range(len(inorder)):
            if val == inorder[i]:
                return i

        return -1

    def helper(self, preorder, pre_start, pre_end, inorder, in_start, in_end):
        # base case
        if pre_start > pre_end or in_start > in_end:
            return None

        root = TreeNode(val=preorder[pre_start])
        idx = self.get_root_index(inorder, preorder[pre_start])
        nums_in_left = idx - in_start

        root.left = self.helper(
            preorder,
            pre_start + 1,
            pre_start + nums_in_left,
            inorder,
            in_start,
            idx - 1,
        )
        root.right = self.helper(
            preorder, pre_start + nums_in_left + 1, pre_end, inorder, idx + 1, in_end
        )

        return root

    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # for better TC create a hashmap/dictionary of inorder
        # to get the index of root in O(1) time
        return self.helper(preorder, 0, len(preorder) - 1, inorder, 0, len(inorder) - 1)
