class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.strip()
        i = 0
        isNegative = False
        start = False
        num = 0
        nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        if s == "":
            return 0
        # 2 Determine if the first character is a + or a -. otherwise assume +
        if s[0] == '+' or s[0] == '-':
            i = 1
            if s[0] == '-':
                isNegative = True

        # 3 skip leading zeros
        for ind in range(i, len(s)):
            dig = ord(s[ind]) - ord("0")
            if dig not in nums:
                break
            elif dig == 0 and not start:
                continue

            else:
                start = True
                num *= 10
                num += dig
                if num > 2 ** 31  or (num >= 2 ** 31 - 1 and not isNegative):
                    if isNegative:
                        return -2 ** 31
                    else:
                        return (2 ** 31) - 1 
        # round really small numbers to -2^31 and big to 2^31 -1 


        if isNegative:
            num *= -1
        return num