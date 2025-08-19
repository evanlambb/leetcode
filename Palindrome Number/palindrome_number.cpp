class Solution {
public:
    bool isPalindrome(int x) {
        if (x < 0) {
            return false;
        }
        vector<int> digs = {};
        while (x > 0) {
            digs.push_back(x % 10);
            x /= 10;
        }
        for (int x: digs) cout << x << " ";

        int l = 0;
        int r = digs.size() - 1;
        while (l <= r) {
            if (digs[l] != digs[r]) {
                return false;
            }
            l++;
            r--;
        }
        return true;
    }
};