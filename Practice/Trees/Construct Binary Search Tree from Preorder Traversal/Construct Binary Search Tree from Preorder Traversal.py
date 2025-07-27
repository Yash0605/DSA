# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# optimal solution
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def bstFromPreorder(self, preorder):
        """
        :type preorder: List[int]
        :rtype: Optional[TreeNode]
        """
        n = len(preorder)
        self.index = 0

        def helper(bound):
            if self.index == n or preorder[self.index] > bound:
                return None

            root = TreeNode(preorder[self.index])
            self.index += 1
            root.left = helper(root.val)
            root.right = helper(bound)

            return root

        return helper(float("inf"))

        """
        root = TreeNode(preorder[0])
        def insert_in_bst(root, val):
            if not root:
                return TreeNode(val)

            if val > root.val:
                root.right = insert_in_bst(root.right,val)
            else:
                root.left = insert_in_bst(root.left,val)

            return root

        for i in range(1,n):
            root = insert_in_bst(root, preorder[i])

        return root
        """


# Educosys solution but in worse case can be O(n^2) if the tree is skewed
class Solution:
    def createTree(self, preorder, start, end):
        if start > end:
            return None

        root = TreeNode(preorder[start])
        # we can have a case where there is no right child, in that case end will be the end of left child
        right_child_start_index = end + 1

        # right subtree will start when the node vals is greater than root vals
        for idx in range(start + 1, end + 1):
            if preorder[idx] > preorder[start]:
                right_child_start_index = idx
                break

        root.left = self.createTree(preorder, start + 1, right_child_start_index - 1)
        root.right = self.createTree(preorder, right_child_start_index, end)

        return root

    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        return self.createTree(preorder, 0, len(preorder) - 1)
