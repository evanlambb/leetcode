class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        character_count = [0] * 26
        l = r = 0
        m = 0
        character_count[ord(s[0]) - ord('A')] += 1
        while r < len(s):
            max_character = 0
            for i in range(26):
                max_character = max(max_character, character_count[i])

            if r - l + 1 - max_character <= k: # we have a valid window...
                m = max(m, r - l + 1)
                r += 1
                if r < len(s):
                    character_count[ord(s[r]) - ord('A')] += 1
            else:
                character_count[ord(s[l]) - ord('A')] -= 1
                l += 1

        return m