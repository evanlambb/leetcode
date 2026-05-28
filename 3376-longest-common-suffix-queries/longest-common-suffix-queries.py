class TreeNode:
    def __init__(self, val: str, ind = 0, word_len = 0):
        self.val = val
        self.neighbours = []
        self.ind = ind
        self.word_len = word_len
class Solution:
    def stringIndices(self, wordsContainer: List[str], wordsQuery: List[str]) -> List[int]:
        minLen = len(wordsContainer[0])
        minInd = 0
        for i, w in enumerate(wordsContainer):
            if len(w) < minLen:
                minLen = len(w)
                minInd = i
        root = TreeNode("")
        for i, word in enumerate(wordsContainer):
            node = root
            for c in word[::-1]: # TODO change this to iterate backwards properly
                found = False
                for n in node.neighbours:
                    if n.val == c:
                        found = True
                        node = n
                        if len(word) < n.word_len: # update the word length 
                            n.ind = i
                            n.word_len = len(word)
                        break
                    

                if not found:
                    # we add the node to the trie
                    node.neighbours.append(TreeNode(c, i, len(word)))
                    node = node.neighbours[-1]
       
        # The trie is properly constructed
        ans = [0] * len(wordsQuery)
        for i, word in enumerate(wordsQuery):
            node = root
            
            # count = 0
            ind = minInd
            for c in word[::-1]:
                found = False
                for n in node.neighbours:
                    if n.val == c:
                        found = True
                        # count += 1
                        ind = n.ind
                        node = n
                if not found:
                    break
            ans[i] = ind
        return ans