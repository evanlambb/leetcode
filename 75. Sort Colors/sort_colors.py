from typing import List

class Solution:
    def swap(self, n1, n2):
        temp = n1
        n1 = n2
        n2 = temp
        return n1, n2

    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        length = len(nums)
        left = 0
        current = 0
        right = length - 1

        while current <= right:
            if nums[current] == 0 and current >= left:
                nums[current], nums[left] = self.swap(nums[current], nums[left])
                left += 1
                continue

                
            elif nums[current] == 2:
                nums[current], nums[right] = self.swap(nums[current], nums[right])
                right -= 1
                continue

            current += 1

        return nums
            
        