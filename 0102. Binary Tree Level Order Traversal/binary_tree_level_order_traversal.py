from typing import Optional, List
from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # just use bfs and add to the list, and then append to the result...
        q = deque()
        q.append((root, 0))
        res = []
        while(q):
            node, lvl = q.popleft()
            if node != None:
                if len(res) == lvl:
                    res.append([])
                res[lvl].append(node.val)
                q.append((node.left, lvl + 1))
                q.append((node.right, lvl + 1))
        return res