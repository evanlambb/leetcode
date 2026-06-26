class Solution:
    def tribonacci(self, n: int) -> int:
        if n == 0:
            return 0
        elif n == 1:
            return 1
        elif n == 2:
            return 1
        fib = [0] * (n+1)
        fib[1] = 1
        fib[2] = 1

        for i in range(2, n + 1):
            fib[i] = fib[i-1] + fib[i-2] + fib[i-3]
        return fib[n]