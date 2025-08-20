# @param {String} s
# @param {String} p
# @return {Integer[]}
def find_anagrams(s, p)
    res = []
    required = {}
    seen = {}

    for i in 0...(p.length)
        if seen.key?(s[i])
            seen[s[i]] += 1
        else
            seen[s[i]] = 1
        end
    end 
    p.each_char do |letter|
        if required.key?(letter)
            required[letter] += 1
        else
            required[letter] = 1
        end 
    end

    l = 0
    r = p.length - 1
    len = s.length
    while r < len
        # check equality between the hash maps, if they're equal, append l to the results
        if seen == required
            res.push(l)
        end 
        # remove / decrement s[l] and add/ increment s[r]
        seen[s[l]] -= 1
        if seen[s[l]] == 0
            seen.delete(s[l])
        end 
        l += 1

        r += 1
        if r >= len
            break
        end 
        if seen.key?(s[r])
            seen[s[r]] += 1
        else
            seen[s[r]] = 1
        end
    end
    return res
end