class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        i = 0 # the current index to insert into 
        prev = -101
        j = 0
        while j < len(nums):
            while j < len(nums) and nums[j] == prev:
                j += 1
            if j >= len(nums) or prev == nums[j]:
                return i
            else:
                nums[i] = nums[j]
                prev = nums[i]
                i += 1
        return i