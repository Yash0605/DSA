"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""


class Solution:
    def levelOrder(self, root: "Node") -> List[List[int]]:
        if not root:
            return []

        queue = deque([root])
        answer = []

        while queue:
            currentLevelNodes = len(queue)
            temp = []

            for i in range(currentLevelNodes):
                node = queue.popleft()

                if node.children:
                    for child in node.children:
                        queue.append(child)

                temp.append(node.val)

            answer.append(temp)

        return answer
