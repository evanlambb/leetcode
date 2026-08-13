class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        @cache
        def dfs(i : int, buy : bool):
            if i >= len(prices):
                return 0
            elif buy:
                return max(dfs(i+1, not buy) - prices[i], dfs(i+1, buy))
            elif not buy:
                return max(dfs(i+2, not buy) + prices[i], dfs(i+1, buy))
        return dfs(0, True)