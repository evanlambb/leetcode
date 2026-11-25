class Solution:
    def search(self, nums: list[int], target: int) -> int:
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                return mid
            if nums[left] < nums[right]:
                if target > nums[mid]:
                    left = mid + 1
                else:
                    right = mid - 1
            
            else:
                # we have the rotation in our segment of the array
                if nums[mid] >= nums[left]:
                    # then we are in the big portion of the array
                    if target > nums[mid] or target <= nums[right]:
                        left = mid + 1
                    else:
                        right = mid - 1
                else:
                    if target >= nums[left] or target < nums[mid]:
                        right = mid - 1
                    else: 
                        left = mid + 1

        return -1