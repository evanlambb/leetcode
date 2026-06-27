class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        counts = dict()

        for num in nums:
            if num in counts: 
                counts[num] += 1
            else:
                counts[num] = 1
        maxLen = 1
        
        
        if 1 in counts:
            if counts[1] % 2 == 0:
                counts[1] -= 1
            maxLen = max(maxLen, counts[1])
        for k in counts.keys():
            if k == 1:
                continue
            currLen = 0
            n = k
            p = 2
            while(n in counts and counts[n] >= 2):
                n = pow(n, p)
                currLen += 2
            if n in counts and counts[n] == 1:
                currLen += 1
            else:
                currLen -= 1
            maxLen = max(maxLen, currLen)

        return maxLen