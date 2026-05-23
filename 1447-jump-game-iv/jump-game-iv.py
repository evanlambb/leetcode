class Solution:
    def minJumps(self, arr: List[int]) -> int:
        q = collections.deque()
        seen = set()
        numbers = DefaultDict(list)

        for i, num in enumerate(arr):
            numbers[num].append(i)

        seen.add(0) # the index that we have seen already
        q.append(0) # tuple (index, steps)
        steps = 0
        while q:
            for _ in range(len(q)):
                index = q.popleft()
                if index == len(arr) - 1:
                    return steps
                else:
                    # search behind, infront, and all of the other similar values
                    nums = numbers[arr[index]] # all other indexes with the same value 
                    for i in range(len(nums) -1, -1, -1):
                        if nums[i] != index and nums[i] not in seen:
                            seen.add(nums[i])
                            q.append(nums[i])
                    numbers[arr[index]] = []

                    if index + 1 not in seen:
                        seen.add(index + 1)
                        q.append(index + 1)
                    
                    if index != 0 and index - 1 not in seen:
                        seen.add(index - 1)
                        q.append(index - 1)
                    
            steps += 1

        return -1