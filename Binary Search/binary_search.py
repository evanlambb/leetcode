class Solution(object):
    def find(self, start, end, lst, target):
        middle = (start + end) / 2

        if lst[middle] == target:
            return middle

        elif start >= end:
            return -1

        elif target > lst[middle]: ## search to the right of middle
            return find(self, middle + 1, end, lst, target)
        else: ## search to the left of middle
            return find(self, start, middle - 1, lst, target)


    # recursive binary search
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        return self.find(0, len(nums) - 1, nums, target)
        
