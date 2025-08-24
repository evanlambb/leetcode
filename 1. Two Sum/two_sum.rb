# @param {Integer[]} nums
# @param {Integer} target
# @return {Integer[]}
def two_sum(nums, target)
    seen = {}
    len = nums.length
    for i in 0...len
        compliment = target - nums[i]
        if seen.key?(compliment)
            return [seen[compliment], i]
        else 
            seen[nums[i]] = i
        end 

    end
    return [-1, -1]
end