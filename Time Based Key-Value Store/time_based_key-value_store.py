class TimeMap:

    def __init__(self):
        self.items = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.items.keys():
            self.items[key] = []
        self.items[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.items.keys():
            return ""
        lst = self.items[key]

        # now just return that timestamp, or previous, or ""
        l = 0
        r = len(lst) - 1
        mid = -1

        while l <= r:
            mid = l + (r - l) // 2
            if lst[mid][1] == timestamp:
                # We found it!
                return lst[mid][0]

            elif timestamp < lst[mid][1]:
                    r= mid - 1
            else:
                l = mid + 1

        # it was not found... I need to look to the prev instance for the list
        if lst[mid][1] < timestamp:
            return lst[mid][0]

        else:
            if mid > 0:
                return lst[mid - 1][0]
            return ""


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)