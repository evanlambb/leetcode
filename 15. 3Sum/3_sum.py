from typing import List

class Solution:

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                # we have already found all of these solutions...
                continue
            else:
                # we can search for new solutions
                l = i + 1
                r = len(nums) - 1

                while l < r:
                    threeSum = nums[i] + nums[l] + nums[r]
                    if threeSum == 0:
                        res.append([nums[i], nums[l], nums[r]])
                        l += 1
                        while l < len(nums) and nums[l] == nums[l - 1]:
                            l += 1 
                    elif threeSum < 0:
                        l += 1
                    else:
                        r -= 1



        return res
        