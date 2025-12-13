from typing import List

class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = zip(position, speed)

        # we now have the cars sorted by their starting position  
        cars = sorted(cars, key=lambda x: x[0])

        # we simply iterate the list backwards, checking if the current time < the last time 
        count = 0
        prev_time = float("-inf")

        for i in range(len(cars)):
            pos, s = cars.pop()
            time = float((target - pos) / s)
            if time > prev_time:
                count += 1
                prev_time = time
                

        return count

