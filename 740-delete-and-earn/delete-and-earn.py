class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        count = dict()
        i = 0
        while i < len(nums):
            if nums[i] in count:
                count[nums[i]] += 1
                nums.pop(i)
            else:
                count[nums[i]] = 1
                i += 1

        sorted_nums = sorted(nums)
        dp = [0] * len(sorted_nums)

        for i in range(len(dp)):
            if i == 0:
                dp[i] = sorted_nums[i] * count[sorted_nums[i]]
            elif i == 1:
                if sorted_nums[i] - sorted_nums[i-1] == 1:
                    dp[i] = max(sorted_nums[i] * count[sorted_nums[i]], dp[i-1])
                else:
                    dp[i] = dp[i-1] + sorted_nums[i] * count[sorted_nums[i]]
            elif sorted_nums[i] - sorted_nums[i-1] == 1:
                dp[i] = max(dp[i - 2] + sorted_nums[i] * count[sorted_nums[i]], dp[i-1])
            else:
                dp[i] = dp[i-1] + sorted_nums[i] * count[sorted_nums[i]]
        return dp[-1]