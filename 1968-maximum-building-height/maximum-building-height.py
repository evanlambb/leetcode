from collections import defaultdict
from typing import List

class Solution:
    def maxBuilding(self, n: int, restrictions: List[List[int]]) -> int:
        max_height = 0
        restriction = defaultdict(lambda: pow(10, 9))
        
        for i, r in restrictions:
            restriction[i] = min(restriction[i], r)
            
        # 1. Explicitly add boundaries
        restriction[1] = 0
        restriction[n] = min(restriction[n], n - 1)

        sorted_keys = sorted(restriction.keys()) 

        # 2. Forward Pass (Left-to-Right)
        # Update current key based on the PREVIOUS key
        for i in range(1, len(sorted_keys)):
            prev_key = sorted_keys[i-1]
            curr_key = sorted_keys[i]
            
            # The max height is prev_height + distance
            distance = curr_key - prev_key
            restriction[curr_key] = min(restriction[curr_key], restriction[prev_key] + distance)

        # 3. Backward Pass (Right-to-Left)
        # Update current key based on the NEXT key
        for i in range(len(sorted_keys) - 2, -1, -1):
            curr_key = sorted_keys[i]
            next_key = sorted_keys[i+1]
            
            distance = next_key - curr_key
            restriction[curr_key] = min(restriction[curr_key], restriction[next_key] + distance)

        # 4. Peak Calculation
        # Now that 'n' is in sorted_keys, we don't need 'if/else' boundary checks
        for i in range(len(sorted_keys) - 1):
            left = sorted_keys[i]
            right = sorted_keys[i+1]
            height_l = restriction[left]
            height_r = restriction[right]

            # Your original peak logic (cleaned up slightly)
            if height_l > height_r:
                height_l, height_r = height_r, height_l
            
            new_l = left + (height_r - height_l)
            if new_l > right:
                max_height = max(max_height, height_l + right - left)
            else:
                max_height = max(max_height, height_l + (height_r - height_l) + (right - new_l) // 2)
            
        return max_height