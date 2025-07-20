# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        if k == 0:
            return [target.val]

        parentMap = {root: -1}
        answer = []

        queue = deque([root])

        while queue:
            node = queue.popleft()

            if node.left:
                queue.append(node.left)
                parentMap[node.left] = node

            if node.right:
                queue.append(node.right)
                parentMap[node.right] = node

        queue = deque([(target, 0)])
        visited = set()
        visited.add(target)

        while queue:
            node, distance = queue.popleft()

            if distance < k:
                if node.left and node.left not in visited:
                    queue.append((node.left, distance + 1))
                    visited.add(node.left)

                if node.right and node.right not in visited:
                    queue.append((node.right, distance + 1))
                    visited.add(node.right)

                if parentMap[node] != -1 and parentMap[node] not in visited:
                    queue.append((parentMap[node], distance + 1))
                    visited.add(parentMap[node])

            elif distance == k:
                answer.append(node.val)

        return answer
