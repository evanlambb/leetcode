class Solution {
public:
    int maxSubarrayLength(vector<int>& nums, int k) {
     map<int, int> counts = {};
     int l = 0;
     int r = 0;
     int mx_len = 0;

     while (r < nums.size()) {
        counts[nums[r]]++;
        // now we have 2 cases, we are either problematic, or we are good
        if (counts[nums[r]] > k) {
            // problematic
            while (counts[nums[r]] > k) {
                counts[nums[l]]--;
                l++;
            }
        } else {
            // check for mx_len update!
            mx_len = max(mx_len, r - l + 1);
        }
        r++;
     } 
     return mx_len;  
    }
};