class Solution:
    def mergeForward(self, start, endSF, intervals, index, newLst):
        length = len(intervals)
        end = True
        while index < len(intervals):
            if endSF >= intervals[index][0] and intervals[index][1] > endSF:
                # the chain continues!
                endSF = intervals[index][1]
            elif endSF < intervals[index][0] and end:
                # we have found the end of the chain...
                newLst.append([start, endSF])
                end = False
            else: # the chain has ended...
                newLst.append(intervals[index])
            index += 1

        return newLst

    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        newLst = []
       
        if newInterval[1] < intervals[0][1]:
            newLst.append(newInterval)
        for i in range(len(intervals)):
            if newInterval[0] >= intervals[i][0] and newInterval[0] <= intervals[i][1]:
                # We have found the beginning of the chain
                return self.mergeForward(intervals[i][0], newInterval[1], intervals, i, newLst)
            elif i < len(intervals) - 1 and intervals[i][1] < newInterval[0] and newInterval[1] >= intervals[i][1]: #insert in between
                return self.mergeForward(newInterval[0], newInterval[1], intervals, i, newLst)
            else:
                newList.append(intervals[i])

        # insert at the end case.
        newLst.append(newInterval)
        return newLst