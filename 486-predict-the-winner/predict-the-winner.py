class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        l = 0
        r = len(nums) - 1
        def minimax(l, r):
            if l == r:
                return nums[l]
                
            pick_left = nums[l] - minimax(l + 1, r)
            pick_right = nums[r] - minimax(l, r - 1)
            
            return max(pick_left, pick_right)
        return True if minimax(l, r) >= 0 else False