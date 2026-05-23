# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.s = []
        node = root
        while node:
            self.s.append(node)
            node = node.left

    def next(self) -> int:
        root = self.s.pop()
        # we are going to return this value, now we need to look right, and then append all of the relevant nodes to the stack 
        node = root.right
        while node:
            self.s.append(node)
            node = node.left
        return root.val

    def hasNext(self) -> bool:
        return len(self.s) != 0


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()