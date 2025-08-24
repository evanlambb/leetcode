# @param {Integer[][]} image
# @param {Integer} sr
# @param {Integer} sc
# @param {Integer} color
# @return {Integer[][]}
def flood_fill(image, sr, sc, color)
    original_color = image[sr][sc]
    return image if image[sr][sc] == color
    image[sr][sc] = color
    rows = image.length
    cols = image[0].length
    # need to check the 4 surrounding colours and change as needed...
    locations = {
    "up"    => [-1, 0],
    "down"  => [1, 0],
    "left"  => [0, -1],
    "right" => [0, 1]
    }    
    locations.delete("up")    if sr == 0
    locations.delete("down")  if sr == rows - 1
    locations.delete("left")  if sc == 0
    locations.delete("right") if sc == cols - 1

    for location in locations
        if image[sr + location[1][0]][sc + location[1][1]] == original_color
            flood_fill(image, sr + location[1][0], sc + location[1][1], color)
        end 
    end 

    return image
end