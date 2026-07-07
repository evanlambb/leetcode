class Solution:
    def pathsWithMaxScore(self, board: List[str]) -> List[int]:
        MOD = pow(10, 9) + 7
        ROWS, COLS = len(board), len(board[0])
        grid = [[(0,0) for _ in range(COLS + 1)] for _ in range(ROWS + 1)] # stores (score, paths)
        
        for r in range(ROWS - 1, -1, -1):
            for c in range(COLS - 1, -1, -1):
                if r == ROWS -1 and c == COLS-1:
                    grid[r][c] = (0, 1)
                elif board[r][c] != "X":
                    score = max(grid[r][c+1][0], grid[r+1][c][0], grid[r+1][c+1][0])
                    paths = ((grid[r][c+1][0] == score) * grid[r][c+1][1] + 
                             (grid[r+1][c][0] == score) * grid[r+1][c][1] + 
                             (grid[r+1][c+1][0] == score) * grid[r+1][c+1][1])
                    if board[r][c] != 'S' and board[r][c] != 'E':
                        score += int(board[r][c])
                    paths %= MOD
                    if paths == 0:
                        score = 0
                    grid[r][c] = (score, paths)
        return grid[0][0]