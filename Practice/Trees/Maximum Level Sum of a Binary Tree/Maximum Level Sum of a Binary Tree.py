from collections import deque


class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        queue = deque([root])
        max_sum = float("-inf")
        max_level = 1
        level = 1

        while queue:
            level_sum = 0
            for _ in range(len(queue)):
                node = queue.popleft()
                level_sum += node.val
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            if level_sum > max_sum:
                max_sum = level_sum
                max_level = level

            level += 1

        return max_level


# Time Complexity: O(n) where n is the number of nodes in the tree.
# Space Complexity: O(n) for the queue used in level order traversal.
