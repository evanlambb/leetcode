class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        pairs = sorted(pairs, key = lambda x: x[1])
        chain = 0
        prev_mx = -1 * float("inf")
        for i in range(len(pairs)):
            if prev_mx < pairs[i][0]:
                chain += 1
                prev_mx = pairs[i][1]
        return chain