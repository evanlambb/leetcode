class Solution:
    def asteroidsDestroyed(self, mass: int, asteroids: List[int]) -> bool:
        rocks = sorted(asteroids)

        for rock in rocks:
            if mass < rock:
                return False

            mass += rock

        return True