import bisect
from typing import List

class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        res = 0
        intervals = sorted(zip(startTime, endTime, profit))
        cache = {}
        def bfs(i):
            if i == len(intervals):
                return 0
            elif i in cache:
                return cache[i]
            
             # one case where we exclude it...
            res = bfs(i+1)

            # one case where we include it 
            j = bisect.bisect(intervals, (intervals[i][1], -1, -1))
            cache[i] = res = max(res, intervals[i][2] + bfs(j))

            return res

        return bfs(0)
           
        