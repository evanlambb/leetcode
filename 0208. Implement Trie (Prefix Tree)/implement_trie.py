class Node:
    def __init__(self, val = "", isEnd = False):
        self.val = val
        self.children = []
        self.isEnd = isEnd

class Trie:

    def __init__(self):
        self.root = Node()

    def insert(self, word: str) -> None:
        tree = self.root
        i = 0
        while i < len(word):
            progressed = False

            for j in range(len(tree.children)):
                if tree.children[j].val == word[i]: # we have found the word
                    tree = tree.children[j]
                    progressed = True
                    break
            if not progressed:
                tree.children.append(Node(word[i])) 
                tree = tree.children[len(tree.children) - 1]
            i += 1
                
        tree.isEnd = True

    def search(self, word: str) -> bool:
        tree = self.root
        for i, char in enumerate(word):
            progressed = False
            for j in range(len(tree.children)):
                if tree.children[j].val == word[i]: # we have found the word
                    tree = tree.children[j]
                    progressed = True
                    break
            if not progressed:
                return False

        return tree.isEnd

    def startsWith(self, prefix: str) -> bool:
        tree = self.root
        for i, char in enumerate(prefix):
            progressed = False
            for j in range(len(tree.children)):
                if tree.children[j].val == prefix[i]: # we have found the word
                    tree = tree.children[j]
                    progressed = True
                    break
            if not progressed:
                return False

        return True

        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)