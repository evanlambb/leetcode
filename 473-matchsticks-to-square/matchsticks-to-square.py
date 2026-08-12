class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        length = sum(matchsticks) / 4
        matchsticks = sorted(matchsticks, reverse=True)
        seen = dict()
        def dfs(i, g1, g2, g3, g4):
            if i == len(matchsticks):
                return g1 == g2 == g3 == g4
            elif (i, tuple(sorted([g1,g2,g3,g4]))) in seen:
                return seen[(i, tuple(sorted([g1,g2,g3,g4])))]
            elif g1 > length or g2 > length or g3 > length or g4 > length:
                return False
            else:
                ans = (
                dfs(i+1, g1 + matchsticks[i], g2, g3, g4) or 
                dfs(i+1, g1, g2 + matchsticks[i], g3, g4) or 
                dfs(i+1, g1, g2, g3 + matchsticks[i], g4) or 
                dfs(i+1, g1, g2, g3, g4 + matchsticks[i])
                )
                seen[(i,tuple(sorted([g1,g2,g3,g4])))] = ans
                return ans

        return dfs(0,0,0,0,0)