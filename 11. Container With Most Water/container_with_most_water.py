class Solution:
    def maxArea(self, height) -> int:
        left = 0
        right = len(height) - 1
        max_sf = 0

        while left < right:
            if min(height[left], height[right]) * (right - left) > max_sf:
                max_sf = min(height[left], height[right]) * (right - left)
            if height[left] > height[right]:
                right -= 1
            else:
                left += 1

        return max_sf