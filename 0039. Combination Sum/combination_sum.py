# This solution did require a video to get from the brute force solution to the optimal solution
from typing import List

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []

        def dfs(cur, total, i):
            if total == target:
                res.append(cur.copy())
                return

            if total > target or i >= len(candidates):
                return

            cur.append(candidates[i])
            dfs(cur, total + candidates[i], i)
            cur.pop()

            dfs(cur, total, i + 1)

        dfs([], 0, 0)
        return res