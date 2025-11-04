import heapq

class MedianFinder:

    def __init__(self):
        self.small, self.large = [], []

    def addNum(self, num: int) -> None:
        # heapq.heappush(heap, val)
        # add to the small
        small = self.small
        large = self.large
        heapq.heappush(small, -1 * num)
        # check that everything in small is <= everything in large
        if small and large and -1 * small[0] > large[0]:
            val = heapq.heappop(small) * -1
            heapq.heappush(large, val)
        # check that the length differs by at most one
        if len(small) > len(large) + 1:
            # The small heap is too long
            val = heapq.heappop(small) * -1
            heapq.heappush(large, val)
        if len(large) > len(small) + 1:
            val = heapq.heappop(large)
            heapq.heappush(small, val * -1)

    def findMedian(self) -> float:
        if len(self.small) == len(self.large):
            return (self.small[0] * -1 + self.large[0]) / 2
        elif len(self.small) > len(self.large):
            return self.small[0] * -1
        return self.large[0]


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()