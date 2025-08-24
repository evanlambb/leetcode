// The API isBadVersion is defined for you.
// bool isBadVersion(int version);

class Solution {
public:
    int firstBadVersion(int n) {
        int left = 1;
        int right = n;

        while (left <= right) {
            int middle = left + (right - left) / 2;
            if (!isBadVersion(middle)) {
                // check to the right...
                left = middle + 1;

            } else {
                // check to the left...
                // we might have the first bad version!
                if (middle == 1) {
                    return 1;
                }
                if (!isBadVersion(middle - 1)) {
                    return middle;
                } else {
                    right = middle - 1;
                }
            }
        }
        return -1;
    }
};