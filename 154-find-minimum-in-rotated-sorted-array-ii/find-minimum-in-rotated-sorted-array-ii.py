class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = l + (r - l) // 2
            if nums[l] < nums[r] or l == r:
                return nums[l]
            else: # we have a rotation still...
                if mid >= 1 and nums[mid] < nums[mid - 1]:
                    return nums[mid]
                if nums[l] == nums[r] == nums[mid]:
                    #return min(self.findMin(nums[l:mid]), self.findMin(nums[mid + 1 : r + 1]))
                    x = min(nums[mid], nums[l]) if mid - l <= 1 else self.findMin(nums[l:mid]) 
                    y = min(nums[mid], nums[r]) if r - mid <= 1 else self.findMin(nums[mid + 1 : r + 1])
                    return min(x, y)
                else:
                    if nums[mid] > nums[r]:
                        l = mid + 1
                    else:
                        r = mid - 1