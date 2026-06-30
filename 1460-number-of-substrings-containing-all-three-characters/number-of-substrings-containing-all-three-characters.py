class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        l, r = 0, -1
        ans = 0
        counts = defaultdict(int) # map the letter -> count 

        while r < len(s):
            if counts['a'] >= 1 and counts['b'] >= 1 and counts['c'] >= 1:
                ans += len(s) - r
                counts[s[l]] -= 1
                l += 1

            else:
                r += 1
                if r < len(s):
                    counts[s[r]] += 1

        return ans