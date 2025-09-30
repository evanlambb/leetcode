# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if p.val > q.val:
            temp = p
            p = q
            q = temp
        # we now know that p.val < q.val

        def search(node):
            if node.val > p.val and node.val < q.val:
                return node
            elif node.val == p.val:
                return p
            elif node.val == q.val:
                return q
            elif node.val > p.val and node.val > q.val:
                # search left
                return search(node.left)
            else:
                return search(node.right)

        return search(root)