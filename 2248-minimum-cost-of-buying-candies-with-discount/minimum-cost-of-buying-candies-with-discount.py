class Solution:
    def minimumCost(self, cost: List[int]) -> int:
        candies = sorted(cost)
        c = 0
        j = 0
        for i in range(len(candies)-1, -1, -1):
            if j == 2:
                j -= 2
                continue
            else:
                c += candies[i]
                j += 1

        return c