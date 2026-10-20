from collections import deque

# implementation of a BST



class Node():
    def __init__(self, key= 0, val=0, left=None, right=None):
        self.key = key
        self.val =val
        self.left = left 
        self.right = right

class BST():
    def __init__(self):
        self.root = None
    def print(self):
        node = self.root

        q = deque()
        q.append(node)
        while len(q) != 0:
            node = q.popleft()

            print(f"{node.key} : {node.val}")
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        print()

    def _insert(self, node, key, value):
            # if not node:
            #     self.root = Node(key, value)
            #     return self.root
        
            if key > node.key:
                # search to the right
                if not node.right:
                    node.right = Node(key, value)
                    return node.right
                return self._insert(node.right, key, value)
            else:
                # search to the left
                if not node.left:
                    node.left = Node(key, value)
                    return node.left
                return self._insert(node.left, key, value)

    def insert(self, key, value):
        node = self.root
        if not node:
            self.root = Node(key, value)
            return self.root
        return self._insert(node, key, value)


    def _delete(self, node, key):
        if not node:
            return
        # traverse to the node that you want to delete
        if key == node.key:
            # swap the root node with the next node in the inorder traversal and delete the old root
            prev = node

            node = node.right
            if not node
        elif key > node.key:
            self._delete(node.right, key)
        else:
            self._delete(node.left, key)


    def delete(self, key):
        node = self.root
        if not node:
            return
        self._delete(node, key)

        # finish implementation

    def search(self, key):
        node = self.root
        while node and node.key != key:
            if key > node.key:
                node = node.right
            else:
                node = node.left
        # other logic that might make sense is to return node.val
        return node if node else None



bst = BST()
bst.insert(4,"a")
bst.print()
bst.insert(3, "b")
bst.print()
bst.insert(1, "c")
bst.print()
bst.insert(5,"d")
bst.print()