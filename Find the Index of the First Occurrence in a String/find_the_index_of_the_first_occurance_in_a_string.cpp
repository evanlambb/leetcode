#include <string>

class Solution {
public:
    int strStr(std::string haystack, std::string needle) {
        int h_length = haystack.size();
        int n_length = needle.size();
        for (int i = 0; i < h_length; i++) {
            bool made_it = true;
            for (int j = 0; j < n_length; j++) {
                if (haystack[i + j] != needle[j]) {
                    made_it = false;
                    break;
                }
            }
            if (made_it) {
                return i;
            }
        }
        return -1;
    }
};