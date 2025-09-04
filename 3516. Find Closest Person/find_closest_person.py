class Solution:
    def findClosest(self, x: int, y: int, z: int) -> int:
        # just find the abs distance between the people, return 1 if x, 2 if y and 0 if its a tie
        dist1 = abs(z-x)
        dist2 = abs(z-y)

        if dist1 > dist2:
            return 2
        elif dist2 > dist1:
            return 1
        return 0