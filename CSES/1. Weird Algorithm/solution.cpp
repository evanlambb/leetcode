#include <bits/stdc++.h>
using namespace std;

int main() {
    long long n;
    cin >> n;

    while (n != 1) {
      cout << n << " ";
      if (n % 2 == 0) {
        // this is the even case
        n /= 2;
      } else {
        // this is the odd case
        n *= 3;
        n += 1;
      }
    }

    cout << "1" << endl;

    return 0;
}