# @param {Integer[]} nums
# @param {Integer} k
# @return {Integer}
def missing_multiple(nums, k)
    largest = 0
    multiples = []
    for num in nums
        largest = num if num > largest
    end
    puts largest
    n = 1
    while k * (n - 1) <= largest
        multiples << k * n
        n += 1
    end
    puts multiples

    for num in nums
        if multiples.include?(num)
            multiples.delete(num)
        end
    end

    return multiples[0]
end