class Solution:
    def maximumElementAfterDecrementingAndRearranging(self, arr: List[int]) -> int:
        sorted_arr = sorted(arr)
        curr = 1
        sorted_arr[0] = 1
        for i in range(len(sorted_arr)):
            if i != 0 and sorted_arr[i] - sorted_arr[i-1] <= 1:
                continue
            elif i != 0:
                sorted_arr[i] = sorted_arr[i- 1] + 1
        return sorted_arr[-1]