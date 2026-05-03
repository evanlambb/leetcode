from typing import List

class Solution:
    def candy(self, ratings: List[int]) -> int:
        prev = -1 # previous rating
        candies = 0 # total candies
        prev_cand = 0 # prev candies 
        peak = 0 # peak index 
        peak_cand = 0 # peak 
        for i, rating in enumerate(ratings):
            if rating > prev:
                candies += (prev_cand + 1)
                peak = i
                peak_cand = prev_cand + 1

                # update the previous
                prev_cand += 1
                prev = rating
            elif rating == prev:
                candies += 1
                peak = i
                peak_cand = 1
                prev_cand = 1
                peak_cand = 1
            else:

                # logic to look at the peak
                if not (peak_cand >= i - peak + 1): # include peak
                    candies += 1
                    peak_cand += 1
                candies += (i - peak)

                # update the previous
                prev_cand = 1
                prev = rating

        return candies