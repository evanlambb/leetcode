import heapq
class Solution:
    def minCostConnectPoints(self, points: list[list[int]]) -> int:
        cost = 0
        h = [] # (w, x, y)
        seen = set()
        x,y = points[0]
        seen.add((x,y))

        for x2, y2 in points:
            if (x2, y2) in seen:
                continue
            weight = abs(x - x2) + abs(y - y2)
            heapq.heappush(h, (weight, x2, y2))

        while len(h) > 0:
            w,x,y = heapq.heappop(h)
            if (x,y) in seen:
                continue
            cost += w
            seen.add((x,y))
            for x2, y2 in points:
                if (x2, y2) in seen:
                    continue
                weight = abs(x - x2) + abs(y - y2)
                heapq.heappush(h, (weight, x2, y2))



        return cost