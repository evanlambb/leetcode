class RandomizedSet:

    def __init__(self):
        self.seen = dict()
        self.nums = []

    def insert(self, val: int) -> bool:
        if val in self.seen:
            return False
        self.seen[val] = len(self.nums)
        self.nums.append(val)
        return True


    def remove(self, val: int) -> bool:
        # swap the last element with val
        if val not in self.seen:
            return False
        i1 = self.seen[val]
        i2 = len(self.nums) - 1
        val2 = self.nums[i2]
        self.seen[val2] = i1

        temp = self.nums[i1]
        self.nums[i1] = self.nums[i2]
        self.nums[i2] = temp
        # remove the last element
        self.seen.pop(val)
        self.nums.pop()
        return True
    def getRandom(self) -> int:
        ind = random.randint(0, len(self.nums) - 1)
        return self.nums[ind]


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()