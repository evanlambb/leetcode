class Solution:
    def totalWaviness(self, num1: int, num2: int) -> int:
        count = 0
        for i in range(max(num1, 100), num2 + 1):
            num = str(i)
            for j in range(1, len(num) - 1): # all of the candidates for a number
                if (int(num[j- 1]) > int(num[j]) and int(num[j+1]) > int(num[j])) or (int(num[j- 1]) < int(num[j]) and int(num[j+1]) < int(num[j])):
                    count += 1

        return count