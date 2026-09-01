class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        boats = 0
        l ,r = 0, len(people) - 1

        while l <= r:
            if people[l] + people[r] <= limit and l != r:
                l += 1
                r -= 1
            else:
                r -= 1
            boats += 1

        return boats