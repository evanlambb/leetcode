class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        change = [0,0,0]
        
        for bill in bills:
            if bill == 5:
                change[0] += 1
            elif bill == 10:
                # we give change of $5
                if change[0] > 0:
                    change[0] -=1 
                    change[1] += 1
                else:
                    return False
            elif bill == 20:
                # we give change of $15, prioritizing using up the $10 bills 
                if change[0] > 0 and change[1] > 0:
                    change[0] -= 1
                    change[1] -= 1
                    change[2] += 1 # this is redundant and never used

                elif change[0] >= 3:
                    change[0] -= 3
                    change[2] += 1

                else:
                    return False
        return True