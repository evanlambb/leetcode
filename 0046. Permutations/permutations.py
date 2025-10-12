from typing import List
import copy

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []

        def dfs(nums: List[int], sol_sf: List[int]):
            if not nums:
                ans.append(sol_sf)

            else:
                for num in nums:
                    n2 = copy.deepcopy(nums)
                    n2.remove(num)
                    dfs(n2, sol_sf + [num])
                    

        dfs(nums, [])
        return ans