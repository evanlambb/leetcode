class Solution:
    # similar to walls and gates, and rotting oranges
    # multi source BFS

    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(mat), len(mat[0])

        q = deque()
        res = [[-1] * COLS for _ in range(ROWS)]

        for r in range(ROWS):
            for c in range(COLS):
                if mat[r][c] == 0:
                    # it is a water...
                    res[r][c] = 0
                    q.append([r, c])


        while q:
            r, c = q.popleft()
            h = res[r][c]
            neighbours = [[r, c + 1], [r + 1, c], [r - 1, c], [r, c - 1]]
            for neighbour in neighbours:
                nr, nc = neighbour
                if (nr >= 0 and nr < ROWS and nc >= 0 and nc < COLS) and res[nr][nc] == -1:
                    res[nr][nc] = h + 1
                    q.append(neighbour)

        return res