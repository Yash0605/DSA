# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        '''
        Iterative approach
        we need 2 stacks
        one stack traverses the tree
        and other stack keeps track traversal for which node is completed
        '''
        if not root:
            return []
        result, mainStack, pathStack = [], [], []

        mainStack.append(root)

        while mainStack:
            node = mainStack[-1]
            if pathStack and node == pathStack[-1]:
                result.append(node.val)
                mainStack.pop()
                pathStack.pop()
            else:
                # traversal pending
                pathStack.append(node)
                if node.right:
                    mainStack.append(node.right)
                if node.left:
                    mainStack.append(node.left)

        return result
                
        