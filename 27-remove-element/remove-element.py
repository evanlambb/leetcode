class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        dead = len(nums) - 1
        while dead >= 0 and nums[dead] == val:
            dead -= 1
        for i in range(len(nums)):
            if i >= dead:
                break
            if nums[i] == val:
                nums[i] = nums[dead]
                nums[dead] = val # this is not needed
                while dead >= 0 and nums[dead] == val:
                    dead -= 1

        return dead + 1