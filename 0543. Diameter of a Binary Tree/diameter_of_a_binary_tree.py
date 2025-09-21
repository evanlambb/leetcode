from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def __init__(self):
        self.res = 0
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def dfs(node):
            if node == None:
                return 0
            else:
                l = dfs(node.left)
                r = dfs(node.right)

                self.res = max(self.res, l + r)
                return 1 + max(l, r)

        dfs(root)
        return self.res
        