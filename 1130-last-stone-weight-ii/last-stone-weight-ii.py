class Solution:
    def lastStoneWeightII(self, stones: list[int]) -> int:
        s = sum(stones)
        goal = s / 2
        print(goal)


        @cache
        def dfs(i, weight):
            if weight == goal:
                # print(weight)
                return goal
            elif i >= len(stones):
                return weight
            else:
                inc = dfs(i + 1, weight + stones[i])
                skip = dfs(i + 1, weight)

                if abs(goal - inc) < abs(goal - skip):
                    return inc
                return skip
        res = dfs(0,0)

        return int(abs(s - 2 * res))