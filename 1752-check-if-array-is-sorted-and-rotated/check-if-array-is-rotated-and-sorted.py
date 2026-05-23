class Solution:
    def check(self, nums: List[int]) -> bool:
        base = nums[0]
        rotations = 0
        minBeforeRotation = nums[0]
        for num in nums:
            if base > num:
                rotations += 1
            elif rotations == 0:
                minBeforeRotation = min(minBeforeRotation, num)
            if rotations == 1 and num > minBeforeRotation or rotations >= 2:
                return False
            base = num

        return True