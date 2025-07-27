# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    '''
    We can create a list and store the preorder traversal at the start and then perfrom the ops => Time efficient but not space efficient
    For space efficiency => rather than storing entire tree we can simulate the in-order traversal using a controlled recursion with a stack, 
    only storing up to height of tree nodes at a time
    Time:
        next(): O(1) amortized (O(H) worst-case for pushing nodes from right subtree)
        hasNext(): O(1)
    Space:
        O(H), where H is the height of the tree (log N for balanced BST)
    '''

    def __init__(self, root: Optional[TreeNode]):
        self.stack = []
        self.left_traverse(root)

    def next(self) -> int:
        # self.index+=1
        # return self.in_order_list[self.index]
        top_node = self.stack.pop()

        if top_node.right:
            self.left_traverse(top_node.right)

        return top_node.val

    def hasNext(self) -> bool:
        return len(self.stack) > 0

    def left_traverse(self, node):
        while node:
            self.stack.append(node)
            node = node.left

    # def traverse(self, root):
    #     if not root:
    #         return None

    #     self.traverse(root.left)
    #     self.in_order_list.append(root.val)
    #     self.traverse(root.right)


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()