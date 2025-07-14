# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        answer = []

        queue = deque([root])

        while queue:
            currentLevel = len(queue)
            temp = []

            for i in range(currentLevel):
                node = queue.popleft()

                if node.left:
                    queue.append(node.left)

                if node.right:
                    queue.append(node.right)

                temp.append(node.val)

            answer.append(temp)

        answer.reverse()

        return answer

# Time Complexity: O(n)
# Space Complexity: O(n)