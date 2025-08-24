
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

from typing import Optional
class Solution:
    def cloneRec(self, node: Optional['Node'], visited) -> Optional['Node']:
        if node is None:
            return None
        elif node in visited: # maybe i need to verify this more riggorously 
            return visited[node]
        else:
            n = Node(node.val)
            visited[node] = n
            for neighbor in node.neighbors:
                n.neighbors.append(self.cloneRec(neighbor, visited))

            return n


    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        return self.cloneRec(node, {})