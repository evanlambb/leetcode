from typing import List

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        ops = ['+', '-', '*', '/']
        st = []
        for t in tokens:
            if t not in ops: # it is a number
                st.append(t)
            else:
                b = int(st.pop())
                a = int(st.pop())
                if t == "+": res = a + b
                elif t == "-": res = a - b
                elif t == "*": res = a * b
                else: res = a / b

                st.append(res)

        return int(st[0])