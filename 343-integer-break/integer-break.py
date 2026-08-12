class Solution:
    def integerBreak(self, n: int) -> int:
        threes = n // 3
        twos = 0
        remain = n % 3
        if n == 2:
            return 1
        if n == 3:
            return 2
        if remain == 1:
            threes -= 1
            twos = 2
        elif remain == 2:
            twos = 1
        return 3**max(0, threes) * 2**twos