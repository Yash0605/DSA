# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

"""
Different case than LCA in BST
In this case we will have to traverse both left and right subtree
Either of p or q can be ancestor => return ancestor
if both present in left => traverse in left subtree till we get one in left and other in right else need to return None => Edge case in recur func
if both present in right => traverse in left subtree till we get one in left and other in right else need to return None 
    => Need to create fun with this in mind, we cannot return root at the end of the recursive func if we are using the same func
    => or we need to expicitly mention the case where p and q not part of the subtree
    
"""


class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        if not root or p.val == root.val or q.val == root.val:
            return root

        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)

        # if left and right:
        #     return root
        if left and right:
            return root
        if not left and right:
            return right
        return left
