class Solution {
public:
    vector<int> twoSum(vector<int>& numbers, int target) {
        int l = 0;
        int r = numbers.size() - 1;

        while (l < r) {
            int two_sum = numbers[l] + numbers[r];
            if (two_sum == target) {
                return {l + 1, r + 1};
            } else if (two_sum < target) {
                l++;
            } else {
                r--;
            }
        }
        return {-1, -1};
    }
};