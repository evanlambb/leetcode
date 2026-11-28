from collections import deque

class Solution:
    def openLock(self, deadends: list[str], target: str) -> int:
        dead = set(deadends)
        seen = set ()

        q = deque()
        q.append(("0000", 0))
        seen.add("0000")

        while len(q) != 0:
            combo, score = q.popleft()
            # print(combo)
            if combo in dead:
                continue
            elif combo == target:
                return score
            
            l = list(combo)

            for i in range(4):
                l[i] = str((int(l[i]) + 1) % 10)
                new = "".join(l)
                if new not in seen:
                    q.append((new, score + 1))
                    seen.add(new)

                l[i] = str((int(l[i]) + 8) % 10)

                new = "".join(l)
                if new not in seen:
                    q.append((new, score + 1))
                    seen.add(new)
                    
                l[i] = combo[i]

        return -1