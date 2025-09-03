from typing import List

class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        dp = {}
        def dfs(i, sum_sf):
            
            if i == len(nums):
                return 1 if sum_sf == target else 0  # we are at the end and do not want to add any more numbers...
            elif (i, sum_sf) in dp:
                return dp[(i, sum_sf)]

            # We need to look further in the tree... 
            dp[(i, sum_sf)] = dfs(i + 1, sum_sf + nums[i]) + dfs(i + 1, sum_sf - nums[i])
            return dp[(i, sum_sf)]
            


        return dfs(0, 0)
            
        