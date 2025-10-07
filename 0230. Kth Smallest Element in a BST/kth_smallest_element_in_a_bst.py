from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def __init__(self):
        self.rval = 0
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        ans = []
        def dfs(node):
            if len(ans) == k:
                 self.rval = ans[len(ans) - 1]
            if node == None:
                return
            # we always want to look left...
            l = dfs(node.left)
            ans.append(node.val)
            r = dfs(node.right)
            return
        dfs(root)
        return self.rval
            