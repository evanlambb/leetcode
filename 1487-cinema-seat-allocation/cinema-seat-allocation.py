class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:
        families = 2 * n
        lost = set() # stores (row, 1 or 2 or 3) 
        for r, c in reservedSeats:
            if (c == 2 or c == 3 or c == 4 or c == 5) and (r, 1) not in lost:
                families -= 1
                lost.add((r, 1))

                if (r, 1) in lost and (r, 3) in lost and (r,2) not in lost:
                    families += 1
            if (c == 4 or c == 5 or c == 6 or c == 7) and (r,2) not in lost:
                lost.add((r, 2))
                
                if (r,1) in lost and (r,3) in lost:
                    families -= 1
            if (c == 6 or c == 7 or c == 8 or c == 9) and (r,3) not in lost:
                families -= 1
                lost.add((r, 3))

                if (r, 1) in lost and (r, 3) in lost and (r,2) not in lost:
                    families += 1

        return families