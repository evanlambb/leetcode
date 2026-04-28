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
    def connect(self, root: 'Node') -> 'Node':
        q = deque()
        if not root:
            return None
        q.append(root)

        while q:
            prev = None
            for _ in range(len(q)):
                n = q.popleft()
                n.next = prev
                if n.right:
                    q.append(n.right)
                if n.left:
                    q.append(n.left)
                prev = n

        return root