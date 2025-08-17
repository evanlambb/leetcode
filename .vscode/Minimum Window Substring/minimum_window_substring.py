class Solution:
    def minWindow(self, s: str, t: str) -> str:
        left = 0 
        right = 0
        best_start = -1
        best_end = len(s)
        moved_right = True

        if len(t) > len(s):
            return ""

        required = {}
        for letter in t:
            if letter in required:
                required[letter] += 1
            else:
                required[letter] = 1

        while right < len(s):

            if moved_right and s[right] in required.keys():
                required[s[right]] -= 1

            # check if we have everything that we need in the current substring
            has_all = True
            for value in required.values():
                if value > 0:
                    has_all = False
                    break

            if has_all:
                # compare to best
                if best_end - best_start > right - left:
                    best_end = right
                    best_start = left

                # try moving left... 
                if s[left] in required:
                    required[s[left]] += 1
                left += 1
                moved_right = False
                continue

            else:
                # otherwise, we need to move right first to make sure that everything is in the sub string...
                moved_right = True
                right += 1
        if 1 + best_end - best_start <= len(s):
            return s[best_start:best_end + 1]

        return ""
            
            

        