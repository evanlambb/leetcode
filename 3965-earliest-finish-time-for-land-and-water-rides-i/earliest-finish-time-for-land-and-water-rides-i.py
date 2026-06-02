class Solution:
    def earliestFinishTime(self, landStartTime: List[int], landDuration: List[int], waterStartTime: List[int], waterDuration: List[int]) -> int:

        minTime = float('inf')
        land = list(zip(landStartTime, landDuration))
        water = list(zip(waterStartTime, waterDuration))


        for start, dur in land:
            minTime = min(minTime, start + dur)
        minFinalTime = float('inf')

        for start, dur in water:
            if start <= minTime:
                minFinalTime = min(minFinalTime, minTime + dur)
            else:
                minFinalTime = min(minFinalTime, start + dur)

        minTime2 = float('inf')
        for start, dur in water:
            minTime2 = min(minTime2, start + dur)
        minFinalTime2 = float('inf')

        for start, dur in land:
            if start <= minTime2:
                minFinalTime2 = min(minFinalTime2, minTime2 + dur)
            else:
                minFinalTime2 = min(minFinalTime2, start + dur)
        return min(minFinalTime, minFinalTime2)