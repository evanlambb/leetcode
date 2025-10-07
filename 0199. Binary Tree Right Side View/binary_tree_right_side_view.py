from typing import Optional, List
from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # traverse the binary tree level by level, and prioritze the R.H.S

        q = deque()
        if root == None:
            return []
        q.append(root)
        ans = []
        while q:
            for i in range(len(q)): # traverse the single level
                n = q.popleft()
                if i == 0:
                    ans.append(n.val)
                if n.right:
                    q.append(n.right) 
                if n.left:
                    q.append(n.left)
                    
        return ans