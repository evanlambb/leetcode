class Solution:
    def maximumSafenessFactor(self, grid: List[List[int]]) -> int:
        q = collections.deque()
        visited = set()
        ROWS, COLS = len(grid), len(grid[0])
        matrix = [[0 for _ in range(COLS)] for _ in range(ROWS)]
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    visited.add((r,c))
                    q.append((r,c)) # append the tuple 
        dist = -1
        
        while q:
            dist += 1
            for _ in range(len(q)):
                r, c = q.popleft()
                matrix[r][c] = dist
                dr = [1, -1, 0, 0]
                dc = [0, 0, 1, -1]
                for i in range(4):
                    row = r + dr[i]
                    col = c + dc[i]
                    if row >= 0 and row < ROWS and col >= 0 and col < COLS and (row, col) not in visited:
                        q.append((row, col))
                        visited.add((row, col))
        # print(matrix)
        visited.clear()
        h = []
        ans = matrix[0][0]
        h.append((-1 * matrix[0][0], 0,0))
        while h:
            curr, r, c = heapq.heappop(h)
            # print(f"visiting {r}, {c}")
            curr *= -1
            r *= -1
            c *= -1
            ans = min(ans, curr)
            if r == ROWS - 1 and c == COLS - 1:
                return ans
            else:
                dr = [1, -1, 0, 0]
                dc = [0, 0, 1, -1]
                for i in range(4):
                    row = r + dr[i]
                    col = c + dc[i]
                    if row >= 0 and row < ROWS and col >= 0 and col < COLS and (row, col) not in visited:
                        # add it to the heap
                        visited.add((row, col))
                        score = matrix[row][col] * -1
                        row *= -1 
                        col *= -1
                        heapq.heappush(h, (score, row, col))
                        # add it to the visited
        return ans