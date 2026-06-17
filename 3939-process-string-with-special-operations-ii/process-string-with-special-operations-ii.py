class Solution:
    def processStr(self, s: str, k : int) -> str:
        current_length = 0
        stack = []

        for c in s:
            stack.append(current_length)
            if c == '*':
                current_length = max(0, current_length - 1)
            elif c == '#':
                current_length *= 2
            elif c == '%':
                continue
            elif ord(c) >= ord('a') and ord(c) <= ord('z'):
                current_length += 1

        if k > current_length - 1:
            return '.'

        for i in range(len(s) -1, -1, -1):
            l = stack.pop()
            if s[i] == '%':
                k = l - 1 - k
            elif s[i] == '#':
                k -= l if k >= l else 0
            elif k == l:
                return s[i] 

        