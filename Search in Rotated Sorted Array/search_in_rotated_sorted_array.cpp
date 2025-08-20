class Solution {
public:
    int search(vector<int>& nums, int target) {
        int left = 0;
        int right = nums.size() - 1;

        while (left <= right) {
            int middle = left + (right - left) / 2;
            if (nums[middle] == target) {
                return middle;
            } else if (nums[left] <= nums[middle]) { // we are in the left
                if (target > nums[middle] || target < nums[left]) {
                    // search right
                    left = middle + 1;
                } else {
                    right = middle - 1;
                }
            } else { // we are in the right
                if (target > nums[right] || nums[middle] > target) {
                    // search left
                    right = middle - 1;
                } else {
                    left = middle + 1;
                }
            }
        }
        return -1;
    }
};