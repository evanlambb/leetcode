# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: TreeNode | None) -> list[int]:
        # left, right, self
        ans = []

        def dfs(node):
            if not node:
                return
            else:
                dfs(node.left)
                dfs(node.right)
                ans.append(node.val)
        dfs(root)
        return ans