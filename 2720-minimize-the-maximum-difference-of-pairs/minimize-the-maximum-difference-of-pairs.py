class Solution:
    def minimizeMax(self, nums: List[int], p: int) -> int:
        def isValid(threshold):
            i, count = 0,0

            while i < len(nums) - 1:
                if abs(nums[i] - nums[i+1]) <= threshold:
                    count += 1
                    i += 2
                else:
                    i += 1
                if count == p:
                    return True
            return False

        if p == 0:
            return 0
        nums.sort()
        l, r = 0, nums[-1] - nums[0]
        mx = r

        while l <= r:
            m = l + (r-l) // 2
            if isValid(m):
                r = m - 1
                mx = m
            else:
                l = m + 1
        return mx