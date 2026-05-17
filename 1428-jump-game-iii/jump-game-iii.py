class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        seen = set()

        def dfs(i):
            if i >= len(arr) or i < 0:
                return False
            if arr[i] == 0:
                return True
            if i in seen:
                return False
            seen.add(i)
            return dfs(i + arr[i]) or dfs(i - arr[i])
            # if i + arr[i] not in seen and i - arr[i] not in seen:
            #     return dfs(i + arr[i]) or dfs(i - arr[i])
            # elif i + arr[i] not in seen:
            #     return dfs(i + arr[i])
            # elif i - arr[i] not in seen:
            #     return dfs(i - arr[i])


        return dfs(start)