class Solution:
    def findGCD(self, nums: List[int]) -> int:
        mn, mx = nums[0], nums[0]

        for num in nums:
            mx = max(mx, num)
            mn = min(mn, num)
        # print(f"{mx}, {mn}")
        a = mx
        b = mn
        while True:
            r = a % b
            q = a / b
            if r == 0:
                return int(a / q)
            a = b
            b = r