class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen_sf = {}
        start = 0
        end = 0
        length = len(s)
        best_start = 0
        best_end = -1
        if length == 1:
            return 1

        while end < length:
            if s[end] in seen_sf:
                # we need to iterate and remove until this is not the case
                seen_sf.pop(s[start])
                start += 1
            else:
                # our substring just got bigger!
                seen_sf[s[end]] = 1
                
                # check for new best
                if end - start > best_end - best_start:
                    best_end = end
                    best_start = start
                
                end += 1

        return best_end - best_start + 1

        