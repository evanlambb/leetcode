class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        d = []
        r = []
        
        for i, c in enumerate(senate):
            if c == "D":
                d.append(i)
            else:
                r.append(i)

        term = len(senate) + 1
        

        while len(d) > 0 and len(r) > 0:
            # both parties have characters left
            i, j = 0, 0

            # i corresponds to d
            # j corresponds to r
            while len(d) != 0 and len(r) != 0 and (i != term or j != term):
                if i == term:
                    if len(d) == 0:
                        return "Radiant"
                    d.pop(0)
                    j += 1
                    if j >= len(r):
                        j = term
                elif j == term:
                    if len(r) == 0:
                        return "Dire"
                    r.pop(0)
                    i += 1
                    if i >= len(d):
                        i = term
                else:
                    if d[i] < r[j]:
                        # then we are on a D
                        if len(r) == 0:
                            return "Dire"
                        r.pop(j)
                        if j >= len(r):
                            j = term
                        i += 1
                        if i >= len(d):
                            i = term
                    else:
                        if len(d) == 0:
                            return "Radiant"
                        d.pop(i)
                        if i >= len(d):
                            i = term
                        j += 1
                        if j >= len(r):
                            j = term

        if len(d) != 0:
            return "Dire"
        return "Radiant"