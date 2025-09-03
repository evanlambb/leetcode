class Solution:
    def climbStairs(self, n: int) -> int:
        temp = 0  
        one = 1
        two = 1

        while n > 1: 
            temp = one 
            one += two
            two = temp
            n -= 1

            return one
