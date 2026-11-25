class Solution:
    def setZeroes(self, matrix: list[list[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        r0 = 1

        ROWS, COLS = len(matrix), len(matrix[0])

        for r in range(ROWS):
            for c in range(COLS):
                if matrix[r][c] == 0:
                    if r == 0:
                        r0 = 0
                        matrix[0][c] = 0
                    else:
                        matrix[r][0] = 0
                        matrix[0][c] = 0

        for c in range(1, COLS):
            for r in range(1, ROWS):
                if matrix[0][c] == 0:
                    matrix[r][c] = 0

        for r in range(1, ROWS):
            for c in range(1, COLS):
                if matrix[r][0] == 0:
                    matrix[r][c] = 0
        if matrix[0][0] == 0:
            for r in range(ROWS):
                matrix[r][0] = 0
        if r0 == 0:
            for c in range(COLS):
                matrix[0][c] = 0
        