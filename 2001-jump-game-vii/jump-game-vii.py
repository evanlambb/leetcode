class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        q = deque([0])
        length = len(s)
        farthest = 0

        while q:
            i = q.popleft()
            if i == length - 1:
                return True
            else:
                for ind in range(max(farthest + 1, i + minJump), min(length, i + maxJump + 1)):
                    if s[ind] == "0":
                        q.append(ind)
                    farthest = max(farthest, ind)
        return False
