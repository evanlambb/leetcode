# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minCameraCover(self, root: TreeNode | None) -> int:
        # I think that we are going to try a bottom up traversal to do this
        count = 0
        if root and not root.left and not root.right:
            return 1
        def bottomUp(node : TreeNode | None) -> bool: 
            nonlocal count
            if not node:
                return (True, False) # we are covered by a camera! (there is nothing to cover)
            else:
                l_cover, l_camera = bottomUp(node.left)
                r_cover, r_camera = bottomUp(node.right)
                if node == root and l_cover and r_cover and not l_camera and not r_camera:
                    count += 1
                    return (True, True)
                if not r_cover or not l_cover: # we need a camera here
                    count += 1
                    return (True, True)
                elif l_camera or r_camera:
                    return (True, False)
                else:
                    return (False, False)
        bottomUp(root)
        return count
