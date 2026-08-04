class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        smallest = float('inf')
        largest = -1 * float('inf')

        for num in nums:
            if num < smallest:
                smallest = num
            if num > largest:
                largest = num

        ans = []

        for i in range(smallest, largest + 1):
            ans.append(i)

        for num in nums:
            ans.remove(num)
        return ans