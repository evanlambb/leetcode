class Solution:
    def rotate(self, matrix: list[list[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        
        left, right = 0, len(matrix) - 1
        while left < right:
            for i in range(right - left):
                top, bottom = left, right
                
                topLeft = matrix[top + i][left]

                # move bottom left into top left
                matrix[top + i][left] = matrix[bottom][left + i]

                # bottom right into bottom left
                matrix[bottom][left + i] = matrix[bottom - i][right]

                # top right into bottom right
                matrix[bottom - i][right] = matrix[top][right - i]

                # top left into top right
                matrix[top][right - i] = topLeft

            left += 1
            right -= 1