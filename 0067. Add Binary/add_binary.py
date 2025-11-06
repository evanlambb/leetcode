class Solution:
    def addBinary(self, a: str, b: str) -> str:
        a_list = list(a)
        b_list = list(b)
        if len(a) > len(b):
            b_list = ["0"] * (len(a) - len(b) + 1) + b_list
            a_list = ["0"] + a_list
        else:
            a_list = ["0"] * (len(b) - len(a) + 1) + a_list
            b_list = ["0"] + b_list
        print(a_list)
        print(b_list)

        # so now, the last digit is always a zero for both numbers... 
        ans = ""
        i = len(a_list) - 1
        while i >= 0:
            s = int(a_list[i]) + int(b_list[i])
            ans = str(s % 2) + ans
            if i != 0:
                a_list[i - 1] = str(int(a_list[i - 1]) + s // 2)
            i -= 1
        if ans[0] == "0":
            return ans[1:]
        return ans
