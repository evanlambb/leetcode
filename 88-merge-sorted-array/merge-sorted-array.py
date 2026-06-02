class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        for i in range(m, m + n):
            nums1[i] = nums2[i-m]
            j = i
            while j > 0 and nums1[j] < nums1[j-1]:
                temp = nums1[j]
                nums1[j] = nums1[j-1]
                nums1[j-1] = temp
                j -= 1