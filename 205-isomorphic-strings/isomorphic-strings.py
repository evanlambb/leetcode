class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        mappings = dict()
        if len(s) != len(t):
            return False
        for i in range(len(s)):
            if s[i] in mappings:
                if mappings[s[i]] != t[i]:
                    return False
            else:
                # s[i] not in mappings, we do what we want
                if t[i] in mappings.values():
                    return False
                mappings[s[i]] = t[i]
        return True