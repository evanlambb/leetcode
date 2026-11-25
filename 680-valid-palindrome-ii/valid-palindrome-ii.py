class Solution:
    def validPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1
        while l < r:
            if s[l] == s[r]:
                l += 1
                r -= 1
            else:
                break
        if l >= r:
            return True

        # here we try deleting one of the chars
        l2, r2 = l+1, r

        while l2 < r2:
            if s[l2] == s[r2]:
                l2 += 1
                r2 -= 1
            else:
                break
        if l2 >= r2:
            return True

        l2, r2 = l, r - 1

        while l2 < r2:
            if s[l2] == s[r2]:
                l2 += 1
                r2 -= 1
            else:
                break
        if l2 >= r2:
            return True

        return False
