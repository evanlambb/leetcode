class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        vals = dict()
        for i in range(len(arr)):
            if arr[i] in vals:
                vals[arr[i]].append(i)
            else:
                vals[arr[i]] = [i]
        rank = 1
        for k in sorted(vals.keys()):
            for ind in vals[k]:
                arr[ind] = rank
            rank += 1
        return arr