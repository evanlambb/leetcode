from typing import List

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        ans = []
        temps = [] # List of tuples (temperature, index)

        for ind, temp in enumerate(temperatures):
            ans.append(0)
            while temps and temp > temps[-1][0]: # we have gotten a warmer day!
                t, i = temps.pop()
                ans[i] = ind - i
            temps.append((temp, ind))

        return ans