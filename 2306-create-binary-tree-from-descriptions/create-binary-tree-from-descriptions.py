# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        nodes = dict() # (number : TreeNode) where number is an int
        children = set()
        for item in descriptions:
            parent, child, left = item

            if parent not in nodes:
                nodes[parent] = TreeNode(parent)
            if child not in nodes:
                nodes[child] = TreeNode(child)
            if left == 1:
                nodes[parent].left = nodes[child]
            else:
                nodes[parent].right = nodes[child] 

            if child not in children:
                children.add(child)

        for node in nodes.values():
            if node.val not in children:
                return node