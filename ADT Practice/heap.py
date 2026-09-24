from typing import List

class Heap:
    # Fix 1: Avoid mutable default arguments
    def __init__(self, h: List[int] = None):
        self.h = h if h is not None else []

    def empty(self) -> bool:
        return len(self.h) == 0

    def root(self) -> int:
        return self.h[0] if not self.empty() else -1

    def parent(self, ind: int) -> int:
        return (ind - 1) // 2

    def left_child(self, ind: int) -> int:
        return 2 * ind + 1

    def right_child(self, ind: int) -> int:
        return 2 * ind + 2

    def insert(self, n: int):
        self.h.append(n)
        self.check_up(len(self.h) - 1)

    def check_up(self, ind: int):
        if ind == 0:
            return 
            
        num = self.h[ind]
        parent_ind = self.parent(ind)
        parent = self.h[parent_ind]
        
        if parent < num:
            # Swap
            self.h[ind], self.h[parent_ind] = self.h[parent_ind], self.h[ind]
            
            # Fix 2: Added 'self.' to recursion
            self.check_up(parent_ind)

    # Fix 3: Fixed indentation and implemented the method
    def check_down(self, ind: int):
        left_ind = self.left_child(ind)
        right_ind = self.right_child(ind)
        largest = ind

        # Check if left child exists and is greater than current largest
        if left_ind < len(self.h) and self.h[left_ind] > self.h[largest]:
            largest = left_ind

        # Check if right child exists and is greater than current largest
        if right_ind < len(self.h) and self.h[right_ind] > self.h[largest]:
            largest = right_ind

        # If the largest is not the current index, swap and recurse
        if largest != ind:
            self.h[ind], self.h[largest] = self.h[largest], self.h[ind]
            self.check_down(largest)

    def pop(self) -> int:
        if self.empty():
            return -1 # Or raise an IndexError
            
        # Swap root with last element
        ans = self.h[0]
        self.h[0] = self.h[-1]
        self.h[-1] = ans

        # Remove the previous root (now at the end)
        self.h.pop()
        
        # Restore heap property starting from root
        if not self.empty():
            self.check_down(0)
            
        # Fix 4: Return the popped value
        return ans