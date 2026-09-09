class MyHashSet:

    def __init__(self):
        self.items = [[] for _ in range(10**6)]

    def add(self, key: int) -> None:
        if key not in self.items[key % 10**6]:
            self.items[key % 10**6].append(key)

    def remove(self, key: int) -> None:
        if key in self.items[key % 10 **6]:
            self.items[key % 10 **6].remove(key)

    def contains(self, key: int) -> bool:
        return key in self.items[key % 10**6]


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)