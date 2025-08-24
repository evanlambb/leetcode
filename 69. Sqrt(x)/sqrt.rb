# @param {Integer} x
# @return {Integer}
def my_sqrt(x)
    num = 0
    while num * num <= x
        num += 1
    end 
    num -= 1
    return num
end