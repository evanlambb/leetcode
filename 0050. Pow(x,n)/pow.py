class Solution:
    def myPow(self, x: float, n: int) -> float:
        def helper(x, n):
            if x == 0:
                return 0
            elif n == 0:
                return 1
            else:
                mult = helper(x, n // 2)
                return mult * mult * x if n % 2 else mult * mult
        ans = helper(x, abs(n))
        return ans if n >= 0 else 1/ans