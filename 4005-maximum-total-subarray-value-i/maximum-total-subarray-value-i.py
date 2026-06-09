class Solution:
    def maxTotalValue(self, nums: List[int], k: int) -> int:
        mn, mx = nums[0], nums[0]
        l,r = 0, 0
        for i in range(len(nums)):
            if nums[i] > mx:
                r = i
                mx = nums[i]
            elif nums[i] < mn:
                l = i
                mn = nums[i]

        return (mx - mn) * k