class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        maxPrefix = 0
        prefix = set()

        for num in arr1:
            s = str(num)
            for i in range(1, len(s) + 1):
                if s[:i] not in prefix:
                    prefix.add(s[:i])
        print(prefix)
        for num in arr2:
            s = str(num)
            for i in range(1, len(s) + 1):
                print(f"checking {s[:i]}")
                if s[:i] in prefix:
                    maxPrefix = max(maxPrefix, len(s[:i]))
                else:
                    break

        return maxPrefix