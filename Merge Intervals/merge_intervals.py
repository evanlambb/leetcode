from typing import List

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])
        insert = intervals[0]
        res = []
        for i in range(1, len(intervals)):
            if insert[1] < intervals[i][0]:
                # insert before
                res.append(insert)
                insert = intervals[i]
            else:
                # there is a merge to be done
                insert = min(insert[0], intervals[i][0]), max(insert[1], intervals[i][1])

        res.append(insert)
        return res
            