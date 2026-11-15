from collections import deque

# implementation of a BST



class Node():
    def __init__(self, key= 0, val=0, left=None, right=None):
        self.key = key
        self.val =val
        self.left = left 
        self.right = right
        self.height = 0

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

    def insert(self, key, value):
        self.root = self._insert(self.root, key, value)

    def _insert(self, node, key, value):
        # 1. Perform standard BST insertion[cite: 2]
        if not node:
            return Node(key, value)
        
        if key > node.key:
            node.right = self._insert(node.right, key, value)
        elif key < node.key:
            node.left = self._insert(node.left, key, value)
        else:
            node.val = value # Update value if key exists
            return node

        # 2. Update height and rebalance on the way up[cite: 2]
        return self._rebalance(node)

    def delete(self, key):
        self.root = self._delete(self.root, key)

    def _delete(self, node, key):
        # 1. Search and delete using standard BST logic[cite: 2]
        if not node:
            return node
            
        if key < node.key:
            node.left = self._delete(node.left, key)
        elif key > node.key:
            node.right = self._delete(node.right, key)
        else:
            # Node to delete found
            if not node.left:
                return node.right
            elif not node.right:
                return node.left
            
            # Node with two children: Get the inorder successor[cite: 2]
            temp = self._get_min_value_node(node.right)
            node.key = temp.key
            node.val = temp.val
            node.right = self._delete(node.right, temp.key)

        if not node:
            return node

        # 2. Update height and rebalance on the way up[cite: 2]
        # Note: Delete may require O(height) rotations up the path[cite: 2]
        return self._rebalance(node)

    def _get_min_value_node(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current

    def search(self, key):
        node = self.root
        while node and node.key != key:
            if key > node.key:
                node = node.right
            else:
                node = node.left
        # other logic that might make sense is to return node.val
        return node if node else None



class AVL():
    def __init__(self):
        self.root = None

    def _get_height(self, node) -> int:
        return node.height
    
    def _get_balance(self, node):
        return self._get_height(node.right) - self._get_height(node.left) if node else -1

    def _update_height(self, node):
        node.height = 1 + max(self._get_height(node.left), self._get_height(node.right))

    def _rotate_right(self, z):
        c = z.left
        T = c.right

        c.right = z
        z.left = T

        self._update_height(z)
        self._update_height(c)
        
        return c

    def _rotate_left(self, z):
        c = z.right
        T = c.left

        c.left = z
        z.right = T

        self._update_height(z)
        self._update_height(c)
        
        return c

    def _rebalance(self, node):
        self._update_height(node)
        balance = self._get_balance(node)

        if balance < -1: 
            # we are working with the left rotations
            if self._get_balance(node.left) <= 0:
                # left-left => single left rotation
                return self._rotate_right(node)
            else:
                node.left = self._rotate_left(node.left)
                return self._rotate_right(node)

        elif balance > 1:
            # we are working with right rotations
            if self._get_balance(node.right) >= 0:
                # Right-Right case -> Single Left Rotation
                return self._rotate_left(node)
            else:
                # Right-Left case -> Double Left Rotation[cite: 2]
                node.right = self._rotate_right(node.right)
                return self._rotate_left(node)
        return node


bst = BST()
bst.insert(4,"a")
bst.print()
bst.insert(3, "b")
bst.print()
bst.insert(1, "c")
bst.print()
bst.insert(5,"d")
bst.print()