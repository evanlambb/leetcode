class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1 

        while l <= r:
            mid = l + (r - l) // 2
            
            if nums[mid] == target:
                return mid
            
            # CASE 1: The left half is sorted
            if nums[l] <= nums[mid]:
                # Is the target inside this sorted left half?
                if nums[l] <= target < nums[mid]:
                    r = mid - 1 # Search left
                else:
                    l = mid + 1 # Search right
            
            # CASE 2: The right half must be sorted
            else:
                # Is the target inside this sorted right half?
                if nums[mid] < target <= nums[r]:
                    l = mid + 1 # Search right
                else:
                    r = mid - 1 # Search left
                    
        return -1