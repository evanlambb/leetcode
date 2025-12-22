
class Solution {
public:
    int minEatingSpeed(vector<int>& piles, int h) {
        // it takes koko a minimum of piles.size() hours to eat everything
        // every additional hour is an opportunity to slow down 
        int l = 1;
        int r = -1;
        
        for (auto p : piles) {
            r = max(r, p);
        }
        int ans = r;
        // do the binary search, and then test to see what the time is!
        while (l <= r) {
            int mid = l + (r-l) / 2;
            // now we test if mid would work... 
            double turns = 0;
            for (auto item : piles) {
                turns += ceil(static_cast<double>(item) / static_cast<double>(mid));
            }
            if (turns <= h) {
                ans = min(ans, mid);
                r = mid - 1;
                }
            else if (turns > h) {l = mid + 1;}
        }
        return ans;
    }
};  