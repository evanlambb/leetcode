class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        mx = 0
        for cost in costs:
            mx = max(mx, cost)

        icecreams = [0] * (mx + 1)

        for cost in costs:
            icecreams[cost] += 1
        bought = 0
        i = 0
        while coins > 0 and i < len(icecreams):
            if icecreams[i] != 0:
                if coins >= i:
                    bought += 1
                    icecreams[i] -= 1
                    coins -= i
                else:
                    break
                continue
            i += 1

        return bought