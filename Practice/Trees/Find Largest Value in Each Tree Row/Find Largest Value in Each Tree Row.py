# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        queue = deque([root])
        answer = []

        while queue:
            currentLevelNodes = len(queue)
            currentMax = float("-inf")

            for i in range(currentLevelNodes):
                node = queue.popleft()

                if node.left:
                    queue.append(node.left)

                if node.right:
                    queue.append(node.right)

                currentMax = max(currentMax, node.val)

            answer.append(currentMax)

        return answer
