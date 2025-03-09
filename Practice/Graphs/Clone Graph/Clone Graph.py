"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional


class Solution:
    def cloneGraphUtil(self, node, old_to_new_node_map):
        new_node = Node(node.val)
        old_to_new_node_map[node] = new_node

        for neighbor in node.neighbors:
            # if not cloned
            if neighbor not in old_to_new_node_map:
                new_node.neighbors.append(
                    self.cloneGraphUtil(neighbor, old_to_new_node_map)
                )
            # if node already cloned
            else:
                new_node.neighbors.append(old_to_new_node_map[neighbor])

        return new_node

    def cloneGraph(self, node: Optional["Node"]) -> Optional["Node"]:
        if not node:
            return None

        old_to_new_node_map = {}

        return self.cloneGraphUtil(node, old_to_new_node_map)
