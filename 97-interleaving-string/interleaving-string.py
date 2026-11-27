class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        @cache
        def dfs(i1, i2):
            if len(s1) + len(s2) != len(s3):
                return False
            i3 = i1 + i2
            if i3 >= len(s3):
                return True
            elif i1 < len(s1) and i2 < len(s2):
                if s1[i1] == s3[i3] and s2[i2] == s3[i3]:
                    return dfs(i1+1, i2) or dfs(i1, i2+1)
                elif s1[i1] == s3[i3]:
                    return dfs(i1+1, i2)
                elif s2[i2] == s3[i3]:
                    return dfs(i1, i2+1)
            elif i1 < len(s1):
                if s1[i1] == s3[i3]:
                    return dfs(i1 + 1, i2)
                return False
            elif i2 < len(s2):
                if s2[i2] == s3[i3]:
                    return dfs(i1, i2 + 1)
                return False
            
            return False

        return dfs(0,0)