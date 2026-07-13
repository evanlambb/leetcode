class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        ans = []
        def dfs(num):
            if num >= low and num <= high:
                ans.append(num)
            last = num % 10
            if last == 9:
                return
            last += 1
            num *= 10
            num += last
            dfs(num)
        for i in range(int(str(low)[0]),10):
            dfs(i)

        for i in range(1, int(str(low)[0])):
            dfs(i)
        return sorted(ans)