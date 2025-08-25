class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int, int> seen;  // The key is the number, and the value is the index
        for (int i = 0; i < nums.size(); i++) {  // Iterate through the array
            int compliment = target - nums[i];  // Calculate the complement
            if (seen.find(compliment) != seen.end()) {  // Check if complement exists in the map
                return {seen[compliment], i};  // Return the indices
            } else {
                seen[nums[i]] = i;  // Store the index of the current number
            }
        }
        return {-1, -1};  // Return [-1, -1] if no solution is found
    }
};
