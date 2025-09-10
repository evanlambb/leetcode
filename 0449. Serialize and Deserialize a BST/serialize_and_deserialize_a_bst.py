# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if root == None:
            return f"N "

        else:
            ans = str(root.val) + " " + self.serialize(root.left) + self.serialize(root.right)
            return ans


    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        
        data = data.strip()
        d = data.split()
        self.i = 0
        def dfs():
            if self.i >= len(d) or d[self.i] == 'N':
                return None
            node = TreeNode()

            node.val = int(d[self.i])
            self.i += 1
            node.left = dfs()
            self.i += 1
            node.right = dfs()
            
            return node
        return dfs()
        

# Your Codec object will be instantiated and called as such:
# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# tree = ser.serialize(root)
# ans = deser.deserialize(tree)
# return ans