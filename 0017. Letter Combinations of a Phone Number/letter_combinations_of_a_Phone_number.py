from typing import List

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        letters = {2: ['a', 'b', 'c'], 3: ['d', 'e', 'f'], 
                   4: ['g', 'h', 'i'], 5: ['j', 'k', 'l'],
                   6: ['m', 'n', 'o'], 7: ['p', 'q', 'r', 's'],
                   8: ['t', 'u', 'v'], 9: ['w', 'x', 'y', 'z']}

        digs = list(digits)

        ans = []
        if not digits:
            return []
            

        def dfs(lst, sol_sf):
            if not lst:
                ans.append(sol_sf)
            else:
                for res in letters[int(lst[0])]: 
                    lst_cp = lst[1:].copy()
                    sol_cp = sol_sf
                    sol_cp += res
                    dfs(lst_cp, sol_cp)
        dfs(digs, "")
        return ans