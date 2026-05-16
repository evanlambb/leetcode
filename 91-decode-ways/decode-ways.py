class Solution:
    def numDecodings(self, s: str) -> int:
        seen = dict()
        def dfs(i: int, s: str):
            if i >= len(s):
                return 1
            elif int(s[i]) == 0:
                seen[(s,i)] = 0
                return 0
            elif (s, i) in seen:
                return seen[(s,i)]
            else:
                #print(f"here is s: {s}\n and here is i: {i}\n and here is len(s): {len(s)}\n and here is s[i] {s[i]}" ) 
                if i + 1 < len(s) and (int(s[i]) == 1 or (int(s[i]) == 2 and int(s[i+1]) <= 6)):
                    ans = dfs(i + 1, s) + dfs(i + 2, s)
                    seen[(s,i)] = ans
                    return ans
                else:
                    ans = dfs(i + 1, s)
                    seen[(s,i)] = ans
                    return ans

        return dfs(0, s)
            