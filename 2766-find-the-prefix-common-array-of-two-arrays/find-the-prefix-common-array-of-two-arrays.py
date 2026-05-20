class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        commons = [0] * len(A)
        lost = set()
        matches = len(A) + 1
        prevA, prevB = -1, -1
        for i in range(len(A) -1, -1, -1):
            if prevA not in lost:
                matches -= 1
                lost.add(prevA)
            if prevB not in lost:
                matches -= 1 
                lost.add(prevB)
            if matches == 0:
                break
            commons[i] = matches
            prevA, prevB = A[i], B[i]
        return commons