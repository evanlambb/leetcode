class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        ans = [pivot] * len(nums)
        curr = 0
        for i in range(len(nums)):
            if nums[i] < pivot:
                ans[curr] = nums[i]
                curr += 1
        curr = len(nums) - 1
        for i in range(len(nums) - 1, -1, -1):
            if nums[i] > pivot:
                ans[curr] = nums[i]
                curr -= 1

        return ans