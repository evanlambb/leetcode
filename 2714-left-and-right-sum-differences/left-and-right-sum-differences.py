class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        answer = [0] * len(nums)
        l = 0
        r = sum(nums)
        for i in range(len(nums)):
            if i != 0:
                l += nums[i-1]
            r -= nums[i]
            answer[i] = abs(l - r)

        return answer