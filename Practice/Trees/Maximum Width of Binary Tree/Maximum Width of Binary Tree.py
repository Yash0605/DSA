# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def widthOfBinaryTree(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        queue = deque([(root, 0)])
        maxWidth = 1

        while queue:
            currentLevelNodes = len(queue)
            currentLevelMin = float('inf')
            currentLevelMax = float('-inf')

            for i in range(currentLevelNodes):
                node,val = queue.popleft()

                if i==0:
                    currentLevelMin = val

                # currentLevelMin = min(currentLevelMin, val)
                currentLevelMax = max(currentLevelMax, val)

                if node.left:
                    queue.append((node.left, 2*(val - currentLevelMin)+1))
                    # 2*(val - currentLevelMin) instead of 2*val because in some lang loke java this may overflow for large i/ps 

                if node.right:
                    queue.append((node.right, 2*(val - currentLevelMin)+2))

            maxWidth = max(maxWidth, currentLevelMax - currentLevelMin + 1)

        return maxWidth
        