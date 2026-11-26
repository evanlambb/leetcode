class Node:
        def __init__(self, val='', terminal=True):
            self.val = val
            self.children = []
            self.terminal = terminal


class WordDictionary:
    
    def __init__(self):
        self.trie = Node()

    def addWord(self, word: str) -> None:
        n = self.trie
        for i in range(len(word)):
            # traverse the children
            found = False
            for child in n.children:
                if child.val == word[i]:
                    n = child
                    if i == len(word) - 1:
                        child.terminal = True
                    found = True
            if not found:
                # here is where we start to insert the word... 
                n.children.append(Node(val = word[i], terminal = False))
                if i == len(word) - 1:
                    n.children[-1].terminal = True
                n = n.children[-1]

    def search(self, word: str) -> bool:
        def search_trie(word, trie) -> bool:
            if word == "" and trie.terminal:
                return True
            for letter in word:
                if letter == '.':
                    for child in trie.children:
                        if search_trie(word[1:], child):
                            return True
                    return False
                else:
                    for child in trie.children:
                        if child.val == word[0]:
                            return search_trie(word[1:], child)
                    return False
            return False


        return search_trie(word, self.trie)


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)