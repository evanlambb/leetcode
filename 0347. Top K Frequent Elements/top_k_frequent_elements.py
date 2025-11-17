from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # store a map of the characters that we have seen, and their frequency
        # need an ordered dataset where I can keep the frequencies in order... 
        # keep this in a list of lists?

        positions = {}
        res = []
        orderings = [] # how frequent is the given element...

        for num in nums:
            if num in positions:
                ind = positions[num]
                orderings[ind] += 1 # we have one more of this letter
                while ind > 0 and orderings[ind - 1] < orderings[ind]: # This is the swap case
                    # swap orderings
                    temp = orderings[ind]
                    orderings[ind] = orderings[ind - 1]
                    orderings[ind - 1] = temp
                    
                    # swap res
                    temp = res[ind]
                    res[ind] = res[ind - 1]
                    res[ind - 1] = temp

                    positions[res[ind]] += 1
                    positions[res[ind - 1]] -= 1
                    ind -= 1
            else:
                res.append(num)
                orderings.append(1)
                positions[num] = len(res) - 1

        return res[:k]


