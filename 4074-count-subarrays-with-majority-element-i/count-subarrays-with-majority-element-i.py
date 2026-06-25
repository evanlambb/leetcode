class Solution:
    def countMajoritySubarrays(self, nums: List[int], target: int) -> int:
        Tc = 0
        l, r = 0,0
        ans = 0

        for i in range(len(nums)):
            for j in range(i, len(nums)):
                length = j - i + 1
                if nums[j] == target:
                    Tc += 1
                if length // 2 < Tc:
                    ans += 1
            Tc = 0

        return ans