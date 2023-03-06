#include <iostream>
typedef long long ll;

using namespace std;

int main() {
    int t;
    std::cin >> t;

    ll x, y, res;
    for (int i = 0; i < t; i++) {
        cin >> y >> x;

        if (y > x) {
            if (y % 2) {
                res = (y - 1) * (y - 1) + x;
            } else {
                res = y*y - x + 1;
            }
        } else {
            if (x % 2) {
                res = x*x - y + 1;
            } else {
                res = (x - 1) * (x - 1) + y;
            }
        }

        cout << res << endl;
    }
}
