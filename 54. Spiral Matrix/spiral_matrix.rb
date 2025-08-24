# @param {Integer[][]} matrix
# @return {Integer[]}
def spiral_order(matrix)
    len = 0
    res = []
    h_lim_l = 0
    h_lim_r = matrix[0].length - 1
    v_lim_t = 0
    v_lim_b = matrix.length - 1

    matrix_len = matrix.length * matrix[0].length
    i = 0
    j = 0
    while len < matrix_len
        for i in h_lim_l..h_lim_r
            if len == matrix_len
                break
            end 
            res.push(matrix[j][i])
            len += 1
        end

        v_lim_t += 1

        for j in v_lim_t..v_lim_b
            if len == matrix_len
                break
            end
            res.push(matrix[j][i])
            len += 1
        end

        h_lim_r -= 1

        for i in (h_lim_r).downto(h_lim_l)
            if len == matrix_len
                break
            end
            res.push(matrix[j][i])
            len += 1
        end

        v_lim_b -= 1
        for j in (v_lim_b).downto(v_lim_t)
            if len == matrix_len
                break
            end
            res.push(matrix[j][i])
            len += 1
        end

        h_lim_l += 1
    end

    return res
end