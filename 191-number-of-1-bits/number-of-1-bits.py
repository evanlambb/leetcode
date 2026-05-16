class Solution:
    def hammingWeight(self, n: int) -> int:
        biggest_power = 0
        ones = 0
        while n > 2 ** biggest_power:
            biggest_power += 1
        while n > 0:
            if n >= 2** biggest_power:
                n -= 2 ** biggest_power
                ones += 1
            biggest_power -=1 

        return ones
