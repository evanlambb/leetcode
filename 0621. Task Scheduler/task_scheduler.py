from typing import List
from collections import deque, Counter
import heapq

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        
        count = Counter(tasks)
        maxHeap = [-ctr for ctr in count.values()]
        q = deque() #  each item is [val, time it's ready]
        heapq.heapify(maxHeap)
        time = 0

        while maxHeap or q:
            time += 1

            if maxHeap:
                item = 1 + heapq.heappop(maxHeap)

                if item < 0:
                    q.append([item, time + n])
            if q and q[0][1] == time:  
                heapq.heappush(maxHeap, q.popleft()[0])

        return time

        
        # My Solution 
        
        # # We do the task that has the most of the same first... 

        # # add everything to a dict that is Letter: (count, cooldown)
        # dp = {}
        # c = 0
        # for task in tasks:
        #     if task in dp:
        #         dp[task][0] += 1
        #     else:
        #         dp[task] = [1, 0]

        # while dp:
        #     max_count = 0
        #     task = ''
        #     for key, item in dp.items():
        #         count, cooldown = item
        #         if cooldown <= 0 and max_count < count:
        #             max_count = count
        #             task = key
            
        #     if task:
        #         dp[task][0] -= 1
        #         dp[task][1] = n + 1
        #         if dp[task][0] <= 0:
        #             del dp[task]
            
        #     for t in dp.values():
        #         t[1] -= 1

        #     c += 1

        # return c