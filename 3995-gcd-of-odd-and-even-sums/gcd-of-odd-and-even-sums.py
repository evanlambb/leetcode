class Solution:
    def gcdOfOddEvenSums(self, n: int) -> int:
        sumOdd = 0
        sumEven = 0
        c = 0
        odd = 1
        even = 2
        while c < n:
            sumOdd += odd
            sumEven += even
            odd += 2
            even += 2
            c += 1
        for i in range(sumOdd, 0, -1):
            if sumOdd % i == 0 and sumEven % i == 0:
                return i
        return 1