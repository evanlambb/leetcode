class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefsum = defaultdict(int) # prefix sums that we have seen, and how many
        total = 0
        count = 0
        prefsum[0] = 1

        for num in nums:
            total += num
            prefsum[total] += 1

            target = total - k
            count += prefsum[target]
            if target == total:
                count -= 1

        return count