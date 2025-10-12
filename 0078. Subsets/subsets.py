from typing import List

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = [[]]
        for num in nums:
            for sol in ans:
                # We either choose to include it, or to exclude it...
                cp = sol.copy()
                cp.append(num)
                ans.append(cp)

        return ans
                    