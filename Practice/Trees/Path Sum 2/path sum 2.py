# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def checkPath(self, root, targetSum, current, ans):
        # base case
        if not root:
            return

        current.append(root.val)

        if targetSum == root.val and not root.left and not root.right:
            ans.append(current[:])
            # no return here as we have added node in current so we need to pop it before returning => retuning makes the state inconsistent for further recursion
        else:
            self.checkPath(root.left, targetSum - root.val, current, ans)
            self.checkPath(root.right, targetSum - root.val, current, ans)

        current.pop()

    def pathSum(self, root, targetSum):
        """
        :type root: Optional[TreeNode]
        :type targetSum: int
        :rtype: List[List[int]]
        """
        ans = []
        self.checkPath(root, targetSum, [], ans)
        return ans
