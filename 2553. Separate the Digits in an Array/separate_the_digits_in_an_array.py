from typing import List

class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        ans = []
        for i in range(len(nums) - 1, -1, -1):
            num = nums[i]
            while num > 0:
                ans.append(num % 10)
                num = num // 10

        ans.reverse()
        return ans