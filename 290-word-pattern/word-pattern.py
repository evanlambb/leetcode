class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        map = dict() # letter -> word
        words = s.split()
        seen_words = set()
        if len(pattern) != len(words):
            return False
        for i in range(len(pattern)):
            if pattern[i] not in map and words[i] not in seen_words:
                map[pattern[i]] = words[i]
                seen_words.add(words[i])
            elif pattern[i] in map:
                if map[pattern[i]] != words[i]:
                    return False
            else:
                return False

        return True