class Solution {
public:
    bool searchMatrix(vector<vector<int>>& matrix, int target) {
        int rows = matrix.size();
        int cols = matrix[0].size();
        int length = rows * cols;
        int left = 0;
        int right = length - 1;

        while (left <= right) {
            int mid = left + (right - left) / 2;
            int mid_val = (matrix[mid / cols][mid % cols]);
            if (mid_val == target) {
                return true;
            } else if (mid_val < target) {
                // search left
                left = mid + 1;
            } else {
                // search right
                right = mid - 1;
            }
        }
        return false;
    }
};