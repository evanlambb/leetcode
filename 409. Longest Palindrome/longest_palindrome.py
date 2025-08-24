class Solution:
    def longestPalindrome(self, s: str) -> int:
        seen = {}
        for letter in s:
            if letter in seen:
                seen[letter] += 1

            else:
                seen[letter] = 1

        middle_char = False
        len_sf = 0
        for item in seen.values():
            if item % 2 == 1:
                middle_char = True

            len_sf += int(item / 2) * 2

        if middle_char:
            len_sf += 1
        return len_sf