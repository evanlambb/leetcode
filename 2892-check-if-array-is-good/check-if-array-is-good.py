class Solution:
    def isGood(self, nums: List[int]) -> bool:
        seen = defaultdict(int)

        for n in nums:
            seen[n] += 1
        for i in range(1, len(nums) - 1):
            if seen[i] != 1:
                return False
        
        return seen[len(nums) - 1] == 2