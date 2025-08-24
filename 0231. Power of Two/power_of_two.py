class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n == 1 or n == 2:
            return True
        num = 2

        while n >= num:
            if n == num:
                return True
            num *= 2

        return False