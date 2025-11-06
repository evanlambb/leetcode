from typing import List

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        # for each number, we have 1 case where we add to l1, and another case where we add to l2
        s = 0
        for num in nums:
            s += num
        if s % 2 == 1:
            return False
        else:
            target = s / 2

        dp = {}

        def dfs(i, sum_sf):
            if sum_sf == target:
                return True
            elif sum_sf > target or i >= len(nums):
                return False
            elif (i, sum_sf) in dp:
                return dp[(i,sum_sf)]
            else:
                # This is the recursive case
                a = dfs(i + 1, sum_sf + nums[i]) or dfs(i + 1, sum_sf)
                dp[(i, sum_sf)] = a
                return a

        return dfs(0,0)