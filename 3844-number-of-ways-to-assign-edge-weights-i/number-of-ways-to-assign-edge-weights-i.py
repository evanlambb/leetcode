from collections import defaultdict, deque
from typing import List

class Solution:
    def assignEdgeWeights(self, edges: List[List[int]]) -> int:
        # 1. Build the tree efficiently in O(N) time
        # We don't need 'if x not in' checks because a valid tree has no duplicate edges.
        adj = defaultdict(list)
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
            
        # 2. Find the max depth using an iterative BFS
        # This avoids Python's recursion limit and is very fast.
        max_depth = 0
        queue = deque([(1, -1, 0)]) # (current_node, parent_node, current_depth)
        
        while queue:
            curr, prev, depth = queue.popleft()
            max_depth = max(max_depth, depth)
            
            for neighbor in adj[curr]:
                if neighbor != prev:
                    queue.append((neighbor, curr, depth + 1))
                    
        # 3. Calculate answer using modular exponentiation
        # pow(base, exp, mod) is significantly faster than base**exp % mod
        MOD = 10**9 + 7
        
        # We don't need the conditional for depth <= 2 anymore! 
        # pow(2, 0) is 1, pow(2, 1) is 2, which perfectly aligns with all valid edge counts.
        return pow(2, max_depth - 1, MOD)