class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
    
        while n != 1:
            s = 0
            if n in seen:
                return False
            seen.add(n) 
            for dig in str(n):
                s += int(dig)**2
            n = s
        return True
            