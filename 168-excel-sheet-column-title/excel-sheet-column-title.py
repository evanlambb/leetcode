class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        s = ""
        while columnNumber > 26:
            # print(columnNumber)
            dig = columnNumber % 26
            if dig == 0:
                s += "Z"
                dig = 26
            else:
                s += chr(int(dig + ord("A") - 1))

            columnNumber -= dig
            columnNumber /= 26

        s += chr(int(columnNumber) + ord("A") - 1)
            

        return s[::-1]