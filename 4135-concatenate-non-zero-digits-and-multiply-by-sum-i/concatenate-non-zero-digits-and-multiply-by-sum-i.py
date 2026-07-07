class Solution:
    def sumAndMultiply(self, n: int) -> int:
        x = ""
        s = 0
        for dig in str(n):
            if dig != "0":
                x += dig
                s += int(dig)

        return s * int(x) if x != "" else 0