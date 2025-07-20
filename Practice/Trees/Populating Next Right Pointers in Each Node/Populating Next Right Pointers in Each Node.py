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
    def connect(self, root: "Optional[Node]") -> "Optional[Node]":
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
        # since perfect binary tree we can use next pointers to traverse level by level
        if not root:
            return None

        leftMostNode = root

        while leftMostNode.left:
            current = leftMostNode

            # traversing current level
            while current:
                # linkig current node's left child to right child
                current.left.next = current.right
                if current.next:
                    # linking right child of left node to the left child of right node
                    current.right.next = current.next.left
                # updating the current from left to the right node
                current = current.next

            leftMostNode = leftMostNode.left

        return root
