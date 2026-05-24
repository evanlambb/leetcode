class Solution:
    def maxJumps(self, arr: List[int], d: int) -> int:
        seen = dict() # Index : maximumSteps
        def dfs(i : int):
            if i in seen:
                return seen[i]
            for ind in range(1, d + 1):
                # 2. Make sure that we are not checking something that is not in seen
                if i + ind < len(arr) and arr[i + ind] < arr[i]:
                    if i in seen:
                        seen[i] = max(seen[i], dfs(i + ind) + 1)
                    else:
                        seen[i] = 1 + dfs(i + ind)
                else:
                    break

            for ind in range(1, d + 1):   
                if i - ind >= 0 and arr[i - ind] < arr[i]:
                    if i in seen:
                        seen[i] = max(seen[i], dfs(i - ind) + 1)
                    else:
                        seen[i] = dfs(i - ind) + 1
                else:
                    break
            if i not in seen:
                seen[i] = 1
            return seen[i]


        for i in range(len(arr)):
            dfs(i)  # we are going to see how far we can jump!
        print(seen.values())
        return max(seen.values())