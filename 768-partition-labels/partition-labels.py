from collections import defaultdict
class Solution:
    def partitionLabels(self, s: str) -> list[int]:
        ans = []

        counts = defaultdict(int) # global character counts

        for l in s:
            counts[l] += 1

        partition = dict()

        last = -1
        i = 0

        # print(counts)

        while i < len(s):
            letter = s[i]
            # print(letter)
            if len(partition) == 0 and last == i - 1 or letter not in partition:
                # print("starting new partition")
                partition[letter] = counts[letter] - 1             
            elif letter in partition:
                # print("letter in partition!")
                partition[letter] -= 1
            # else:
            #     print("new character in partition!")
            #     partition[letter] = counts[letter] - 1

            if partition[letter] == 0:
                    # print("exhausted letter!")
                    partition.pop(letter)
                    
                    if len(partition) == 0:
                        # print("end of partition!")
                        ans.append(i - last) # CHECK THIS LOGIC
                        last = i

            # print()
            i += 1

        return ans