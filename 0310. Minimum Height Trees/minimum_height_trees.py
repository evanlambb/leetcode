from typing import List
from collections import deque

class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:

        q = deque()
        neighbours = {}
        num_edges = {}

        if n == 1:
            return [0]

        for edge in edges:
            n1, n2 = edge
            if n1 in neighbours:
                neighbours[n1].append(n2)
                num_edges[n1] += 1
            else:
                neighbours[n1] = [n2]
                num_edges[n1] = 1

            if n2 in neighbours:
                neighbours[n2].append(n1)
                num_edges[n2] += 1
            else:
                neighbours[n2] = [n1]
                num_edges[n2] = 1

        for key, val in num_edges.items():
            if val == 1:
                q.append(key)

        while(n > 2):
            for i in range(len(q)):
                node = q.popleft()
                for nei in neighbours[node]:
                    num_edges[nei] -= 1
                    if num_edges[nei] == 1:
                        q.append(nei)
                n -= 1

        return list(q)