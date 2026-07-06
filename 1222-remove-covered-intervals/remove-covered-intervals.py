class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        sorted_intervals = sorted(intervals)
        i = 0
        while i < len(sorted_intervals) - 1:
            start, end = min(sorted_intervals[i][0], sorted_intervals[i+1][0]), max(sorted_intervals[i][1], sorted_intervals[i+1][1])
            if sorted_intervals[i] == [start, end]:
                sorted_intervals.pop(i+1)
            elif sorted_intervals[i+1] == [start, end]:
                 sorted_intervals.pop(i)
            else:
                i += 1

        return len(sorted_intervals)