class Solution:
    def totalWaviness(self, num1: int, num2: int) -> int:
        def solve(x): # returns the total waviness from 1-x
            n = str(x)
            
            @cache
            def dfs(prev, prevprev, tight, index, lz):
                if index == len(n):
                    # We have placed all of the digits
                    return (1, 0) # (num of valid ways, num of completions)
                else:
                    total_count, total_waves = 0,0
                    upper = int(n[index]) if tight else 9
                    for d in range(upper + 1):
                        new_lz = lz and d == 0
                        new_tight = tight and d == upper
                        if new_lz:
                            new_prev = -1
                        else:
                            new_prev = d
                        new_prevprev = prev
                        new_index = index + 1
                        wave_added = 0
                        if prev != -1 and prevprev != -1:
                            if (prevprev < prev > d) or (prevprev > prev < d):
                                wave_added = 1
                        child_count, child_waves = dfs(new_prev, new_prevprev, new_tight, new_index, new_lz)
                        total_waves += child_waves + child_count * wave_added
                        total_count += child_count
                    return (total_count, total_waves)
            return dfs(-1, -1, True, 0, True)[1]
        return solve(num2) - solve(num1 - 1)
