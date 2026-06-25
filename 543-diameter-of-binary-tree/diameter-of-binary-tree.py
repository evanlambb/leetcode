# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        def dfs(node):
            if node == None:
                return (0, 0) # height, diameter
            else:
                lheight, ldiameter = dfs(node.left)
                rheight, rdiameter = dfs(node.right)

                diam = max(ldiameter, rdiameter, lheight + rheight)
                
                rheight += 1
                lheight += 1

                
                height = max(lheight, rheight)
                return (height, diam)

        return dfs(root)[1]
            