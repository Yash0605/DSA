# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findHeight(self, root):
        if not root:
            return 0

        return 1 + self.findHeight(root.left)

    def countNodes(self, root: Optional[TreeNode]) -> int:
        """
        Optimized solution
        We traverse the left subtree and right subtree
            => case 1 both has same height => this means left is perfect binary tree but right is not => count the nodes of right
            => case 2 when both are not equal i.e left height = right height + 1 => so right is perfect and we need to count the nodes of left

            In a complete binary tree:
                getDepth runs in O(log n)
                At most log n recursive calls
                So, overall time: O(log² n)
        """
        if not root:
            return 0

        heightLeft, heightRight = self.findHeight(root.left), self.findHeight(
            root.right
        )

        if heightLeft == heightRight:
            return pow(2, heightLeft) + self.countNodes(root.right)
        else:
            return pow(2, heightRight) + self.countNodes(root.left)


# Time Complexity: O(log² n) where n is the number of nodes in the tree
# Space Complexity: O(h) where h is the height of the tree due to recursion stack
