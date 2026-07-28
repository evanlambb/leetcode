# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        ans = []
        def dfs(current : str, node):
            if not node:
                return
            if not current:
                current += str(node.val)
            else:
                current += "->" + str(node.val)
            if node and not node.left and not node.right:
                ans.append(current)
                return
            dfs(current, node.left)
            dfs(current, node.right)

        dfs("",root)
        return ans