from typing import List

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        # we loop through the board, if the square is a starting square, we then run DFS on the adjacent squares and save the location in visited set so we do not go there twice... 
        ROWS = len(board)
        COLS = len(board[0])

        def dfs(r, c, i):
            if word[i] != board[r][c]:
                return False
            else:  # we have the next letter!
                i += 1
                if i >= len(word):
                    return True
                neighbours = [(r, c+1), (r,c-1), (r+1, c), (r-1, c)]
                for neighbour in neighbours:
                    nr, nc = neighbour 
                    if nr >= 0 and nr < ROWS and nc >= 0 and nc < COLS and (neighbour not in visited):
                        visited.add((nr,nc))
                        if dfs(nr, nc, i):
                            return True
                        visited.remove((nr,nc))

        for r in range(ROWS):
            for c in range(COLS):
                visited = {(r,c)}
                if dfs(r, c, 0):
                    return True
                else:
                    visited.remove((r,c))

        return False

