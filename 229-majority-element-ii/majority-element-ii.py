class Solution:
    def majorityElement(self, nums: list[int]) -> list[int]:
        # naieve approach, we have a dict that stores the counts
        # if the count hits n/3 we add it
        # Note that we either have 0 or 1 or 2 answers... 

        counts = defaultdict(int)
        ans = []
        for num in nums:
            counts[num] += 1
            if counts[num] == len(nums) // 3 + 1:
                ans.append(num)
        return ans