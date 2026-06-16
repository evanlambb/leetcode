class Solution:
    def processStr(self, s: str) -> str:
        result = ""
        for c in s:
            if c == '*':
                if len(result) > 0:
                    result = result[:-1]
            elif c == '#':
                result += result
            elif c == '%':
                result = result[::-1]
            else:
                result += c
        return result