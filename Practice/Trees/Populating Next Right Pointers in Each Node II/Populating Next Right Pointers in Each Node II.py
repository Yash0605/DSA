"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""


class Solution(object):
    def connect(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        if not root:
            return None

        current = root

        while current:

            dummy = Node(0)
            tail = dummy

            while current:
                if current.left:
                    tail.next = current.left
                    tail = tail.next

                if current.right:
                    tail.next = current.right
                    tail = tail.next

                current = current.next

            current = dummy.next

        return root


"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""


class Solution:
    def connect(self, root: "Node") -> "Node":
        if not root:
            return None

        queue = deque([root])

        while queue:
            currentLevelNodes = len(queue)
            temp = []

            for i in range(currentLevelNodes):
                node = queue.popleft()

                if node.left:
                    queue.append(node.left)

                if node.right:
                    queue.append(node.right)

                temp.append(node)

            if len(temp) > 1:
                for i in range(len(temp) - 1):
                    temp[i].next = temp[i + 1]

        return root
