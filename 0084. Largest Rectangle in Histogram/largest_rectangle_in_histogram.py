from typing import List

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxArea = 0
        stack = [] # (index, height)
        for i, h in enumerate(heights):
            start = i
            while stack and stack[-1][1] > h:
                index, height = stack.pop()
                maxArea = max(maxArea, height * (i - index))
                start = index

            stack.append((start, h))

        for index, height in stack:
            maxArea = max(maxArea, height * (len(heights) - index))

        return maxArea

    # Here was my O(n^2) solution below

    # def largestRectangleArea(self, heights: List[int]) -> int:
    #     max_rect = 0
    #     dp = {}
    #     for i in range(len(heights)):
    #         h = heights[i]
    #         j = i
    #         while j < len(heights) and h > 0:
    #             h = min(h, heights[j])
    #             if j in dp and dp[j] >= h:
    #                 break
    #             max_rect = max(max_rect, h * (j - i + 1))
    #             if j in dp:
    #                 dp[j] = max(dp[j], h)
    #             else:
    #                 dp[j] = h
    #             j += 1
    #         # either we have gotten to the end, or height is now 1... 
    #         # We check a "base case"
    #         # j = len(heights) - 1
    #         # h = 1
    #         # max_rect = max(max_rect, h * (j - i + 1))

    #     return max_rect