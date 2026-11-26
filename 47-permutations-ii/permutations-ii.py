class Solution:
    def permuteUnique(self, nums: list[int]) -> list[list[int]]:
        perms = [[nums[0]]]

        for num in nums[1:]:
            new_perms = []
            for perm in perms:
                for j in range(len(perms[0]) + 1):
                    new = perm[:j] + [num] + perm[j:]
                    new_perms.append(new)
                    if j < len(perm) and perm[j] == num:
                        break
            perms = new_perms
        
        return perms