from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def __init__(self):
        self.ans = True
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        def dfs(node, depth):
            if node == None:
                return 0

            l = dfs(node.left, depth + 1)
            r = dfs(node.right, depth + 1)

            if (abs(l - r) > 1):
                self.ans = False

            return 1 + max(l, r)

        dfs(root, 0)

        return self.ans