# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    '''
    Need to check based on a range
    Initially for the left subtree the values can be present in the range (-inf,root.val)
    Similarly for the right subtree the values can be present in the range (root.val, inf)
    Following this as we can down the subtrees, the ranges will change accordingly for each node
    '''
    def validateBST(self, root, minVal, maxVal):
        if not root:
            return True

        if root.val >= maxVal or root.val <= minVal:
            return False

        return self.validateBST(root.left, minVal, root.val) and self.validateBST(root.right, root.val, maxVal)

    def isValidBST(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        return self.validateBST(root, float('-inf'), float('inf'))
        