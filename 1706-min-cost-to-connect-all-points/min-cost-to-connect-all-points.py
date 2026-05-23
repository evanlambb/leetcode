class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        visited = set()
        h = []
        neighbours = defaultdict(list) 
        
        for i in range(len(points)):
            for j in range(i + 1, len(points)):
                x1, y1 = points[i]
                x2, y2 = points[j]
                manhat = abs(x1 - x2) + abs(y1 - y2)

                neighbours[(x1, y1)].append((manhat, (x2, y2)))
                neighbours[(x2, y2)].append((manhat, (x1, y1)))

        start_point = (points[0][0], points[0][1])
        heapq.heappush(h, (0, start_point))
        dist = 0
        
        while len(visited) < len(points):
            manhat, (x, y) = heapq.heappop(h)
            
            if (x, y) in visited:
                continue
                
            visited.add((x, y))
            dist += manhat
            
            for item in neighbours[(x, y)]:
                if item[1] not in visited:
                    heapq.heappush(h, item)

        return dist