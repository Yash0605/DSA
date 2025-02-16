# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

'''
The reason behind this order is tied to the goal of the algorithm: to find the leftmost value at the last level. 
By enqueueing the right child before the left child, we ensure that nodes at the same level are processed from left to right during the level-order traversal. 
This guarantees that the leftmost value at the last level is encountered first, aligning with the goal of the algorithm.
'''
from collections import deque

class Solution:

    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        q = deque([root])
        ans = None

        while len(q)>0:
            current_node = q.popleft()
            ans = current_node.val

            if current_node.right:
                q.append(current_node.right)

            if current_node.left:
                q.append(current_node.left)

        return ans

    '''
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        q = deque()
        ans = root.val

        q.append(root)

        while len(q)>0:
            current_size = len(q)

            for i in range(current_size):

                current_node = q.popleft()

                if i==0:
                    ans = current_node.val

                if current_node.left:
                    q.append(current_node.left)

                if current_node.right:
                    q.append(current_node.right)

        return ans
        '''

# Time Complexity: O(n)
# Space Complexity: O(n) - in worst case, queue will have all nodes at last level