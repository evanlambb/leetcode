class Solution:
    def majorityElement(self, nums) -> int:
        nums.sort()
        return nums[int(len(nums) / 2)]