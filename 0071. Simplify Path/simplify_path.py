class Solution:
    def simplifyPath(self, path: str) -> str:
        pth = path.split('/')
        stk = []

        for item in pth:
            if not item or item == '.':
                continue
            elif item == "..": # pop from the stack
                if len(stk) != 0:
                    stk.pop()
            else: # add to the stack
                stk.append(item)
                
        ans = ''
        for item in stk:
            ans = ans + '/' + item

        if ans == '':
            return '/'
        return ans