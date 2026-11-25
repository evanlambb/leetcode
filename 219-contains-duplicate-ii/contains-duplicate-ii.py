class Solution:
    def containsNearbyDuplicate(self, nums: list[int], k: int) -> bool:
        seen = dict()

        for i, num in enumerate(nums):
            if num in seen and i - seen[num] <= k:
                return True
            seen[num] = i
        
        return False