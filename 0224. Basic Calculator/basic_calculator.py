class Solution:
    def calculate(self, s: str) -> int:
        current = res = 0
        sign = 1
        stack = []

        for char in s:
            if char.isdigit():
                current = current * 10 + int(char)
            elif char in ["+", "-"]:
                res += sign * current
                current = 0
                if char == "+":
                    sign = 1
                else:
                    sign = -1

            elif char == "(":
                # push current res to stack, and then start the subproblem... 
                stack.append(res)
                stack.append(sign)
                res = 0
                sign = 1
            elif char == ")": # Char == ")"
                res += sign * current
                sign = stack.pop()
                current = res
                res = stack.pop()

        res += sign * current
        return res