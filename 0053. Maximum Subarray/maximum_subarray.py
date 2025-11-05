from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = nums[0]
        current = 0
        for i in range(len(nums)):
            if current < 0:
                current = 0
            current += nums[i]
            max_sum = max(max_sum, current)

        return max_sum
