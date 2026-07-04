class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        graph = dict() # need to map city, to other cities and length
        visited = set()
        # city1 -> [(dist, city2), ...]

        for c1, c2, dist in roads:
            if c1 not in graph:
                graph[c1] = [(dist, c2)]
            else:
                graph[c1].append((dist, c2))
            if c2 not in graph:
                graph[c2] = [(dist, c1)]
            else:
                graph[c2].append((dist, c1))
        
        queue = deque() # heap stores (MinDistance, city)
        queue.append((float('inf'), 1))
        ans = float('inf')
        
        while queue:
            min_distance, city = queue.pop()
            ans = min(ans, min_distance)
            if city in visited:
                continue
            visited.add(city)
           #  print(f"visiting {city} with total distance {min_distance}")
            
            for dist, city2 in graph[city]:
                # visited.add(city2)
                queue.append((min(dist, min_distance), city2))
        return ans
        