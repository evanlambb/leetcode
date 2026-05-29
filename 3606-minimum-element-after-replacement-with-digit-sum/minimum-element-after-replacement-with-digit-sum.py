class Solution:
    def minElement(self, nums: List[int]) -> int:
        minSeen = float('inf')
        for num in nums:
            curr = 0
            for dig in str(num):
                curr += int(dig)
            minSeen = min(minSeen, curr)
        return minSeen