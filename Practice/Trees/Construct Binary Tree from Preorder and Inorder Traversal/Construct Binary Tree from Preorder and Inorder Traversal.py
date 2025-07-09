# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: Optional[TreeNode]
        """
        if len(preorder) == 1:
            return TreeNode(preorder[0])

        inorderIndexMap = {}

        for i in range(len(inorder)):
            currentElement = inorder[i]
            inorderIndexMap[currentElement] = i

        def buildTreeHelper(
            preorder, inorder, preorderStart, preorderEnd, inorderStart, inorderEnd
        ):
            # base case
            if preorderStart > preorderEnd or inorderStart > inorderEnd:
                return None

            root = TreeNode(preorder[preorderStart])
            inorderRootIndex = inorderIndexMap[preorder[preorderStart]]
            leftSubtreeLength = inorderRootIndex - inorderStart

            root.left = buildTreeHelper(
                preorder,
                inorder,
                preorderStart + 1,
                preorderStart + leftSubtreeLength,
                inorderStart,
                inorderRootIndex - 1,
            )
            root.right = buildTreeHelper(
                preorder,
                inorder,
                preorderStart + leftSubtreeLength + 1,
                preorderEnd,
                inorderRootIndex + 1,
                inorderEnd,
            )

            return root

        return buildTreeHelper(
            preorder, inorder, 0, len(preorder) - 1, 0, len(inorder) - 1
        )
# Time Complexity: O(n) where n is the number of nodes in the tree.
# Space Complexity: O(n) for the inorderIndexMap and the recursion stack.