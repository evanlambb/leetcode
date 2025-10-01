# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def __init__(self):
        self.ans = None

    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def dfs(node):
            if node == None:
                return False

            l = dfs(node.left)
            r = dfs(node.right)

            if l and r:
                self.ans = node
                return False
            elif node.val == p.val or node.val == q.val:
                if l or r:
                    self.ans = node
                    return False
                else:
                    return True
            else:
                return l or r

        dfs(root)
        return self.ans
                
            