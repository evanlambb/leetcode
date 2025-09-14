#include "../../../include/print.h"
#include <algorithm>
#include <cmath>
#include <vector>

using namespace std;
using ll = long long;

class Solution {
public:
    long long minOperations(vector<vector<int>> &queries) {
        ll result = 0;
        for (auto &query : queries) {
            ll l = query[0];
            ll r = query[1];
            int k = ceil(log(l) / log(4)); // Represents the power of 4
            ll sum = 0;
            ll i = pow(4, k);
            ll prevI = l;
            while (prevI <= r) {
                ll interval = min(i, r + 1) - prevI;
                sum += (interval * k);
                prevI = i;
                i *= 4;
                k++;
            }
            result += ceil(sum / 2.0);
        }
        return result;
    }
};

int main() {
    Solution s;
    vector<vector<vector<int>>> tests = {// {{1, 2}, {2, 4}},
                                         // {{2, 6}},
                                         {{5, 8}}};
    for (auto &tt : tests) {
        auto result = s.minOperations(tt);
        cout << "Result " << result << "\n";
    }
}