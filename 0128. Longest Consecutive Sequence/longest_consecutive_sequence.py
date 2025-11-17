from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        max_sf = 0
        for num in s:
            count = 0
            if not num - 1 in s: # This is the start of a sequence
                count += 1
                while num + 1 in s:
                    count += 1
                    num += 1
                max_sf = max(max_sf, count)

        return max_sf
        