class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        height : int = 0
        mx_height = 0
        for g in gain:
            height += g
            mx_height = max(mx_height, height)

        return mx_height