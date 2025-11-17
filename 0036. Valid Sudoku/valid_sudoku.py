from typing import List

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # problem with a costant time solution :) O(81) -> O(1)
        # track row posn, col posn, and square posn
        rows = [[] for _ in range(9)]
        cols = [[] for _ in range(9)]
        squares = [[] for _ in range(9)]

        for row in range(9):
            for col in range(9):
                print(f"looking at {board[row][col]}")
                val = board[row][col]
                if val != "." and val in rows[row] or val in cols[col] or val in squares[int(row / 3)  * 3 + int(col / 3)]:
                    return False
                else:
                    # add to the lists
                    rows[row].append(val)
                    cols[col].append(val)
                    squares[int(row / 3) * 3 + int(col / 3)].append(val)

        return True