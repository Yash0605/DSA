# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[Optional[TreeNode]]
        """

        def traverseAndCreateTrees(start, end):
            ans = []
            if start > end:
                root = None
                ans.append(root)
                return ans

            if start == end:
                root = TreeNode(start)
                ans.append(root)
                return ans

            for i in range(start, end + 1):
                left = traverseAndCreateTrees(start, i - 1)
                right = traverseAndCreateTrees(i + 1, end)

                for l in left:
                    for r in right:
                        root = TreeNode(i)
                        root.left = l
                        root.right = r

                        ans.append(root)

            return ans

        return traverseAndCreateTrees(1, n)


# Time Complexity: O(4^n / n^(3/2)), where n is the number of nodes.
# Space Complexity: O(n), for the recursion stack and storing the trees.
