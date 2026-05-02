class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l, r, s = 0, 0, 0
        m = float('inf')
        while r < len(nums):
            if s < target:
                s += nums[r]
                while s >= target:
                    m = min(m, r - l + 1)
                    s -= nums[l]
                    l += 1
                    if s >= target:
                        m = min(m, r - l + 1)
                r += 1
                
        return 0 if m == float('inf') else m
        