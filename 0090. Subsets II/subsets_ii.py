from typing import List

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = []
        
        def dfs(sol: List[int], ind : int):
            # at a given point, we choose to insert the current, or to not do anything... 
            if ind == len(nums):
                ans.append(sol)
                return
            
            # add the number
            s2 = sol.copy()
            s2.append(nums[ind])
            dfs(s2, ind + 1)
            # dont add the number
            s3 = sol.copy()
            while ind + 1 < len(nums) and nums[ind + 1] == nums[ind]:
                ind += 1
            dfs(s3, ind + 1)

        dfs([], 0)
        return ans