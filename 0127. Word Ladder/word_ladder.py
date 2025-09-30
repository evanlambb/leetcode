from typing import List
from collections import deque

class Solution:
    def differsByOne(self, w1, w2) -> bool:
        differInOnePlace = False
        for i in range(len(w1)):
            if w1[i] != w2[i]:
                if differInOnePlace:
                    return False
                differInOnePlace = True
        return True
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordSet = {}

        visited = set()
        Q = deque()
        for i, word in enumerate(wordList):
            if word == beginWord:
                continue

            if word not in wordSet:
                wordSet[word] = []

            # Starting point for the bfs
            if self.differsByOne(word, beginWord):
                Q.append((word, 1))
                visited.add(word)

            for j in range(i + 1, len(wordList)):
                if self.differsByOne(word, wordList[j]):
                    wordSet[word].append(wordList[j])
                    if wordList[j] not in wordSet:
                        wordSet[wordList[j]] = []
                    wordSet[wordList[j]].append(word)

        while Q:
            cur = Q.popleft()
            if cur[0] == endWord:
                return cur[1] + 1


            for adjWord in wordSet[cur[0]]:
                if adjWord not in visited:
                    Q.append((adjWord, cur[1] + 1))
                    visited.add(adjWord)

        return 0