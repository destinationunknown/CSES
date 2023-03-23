#include <iostream>
typedef long long ll;

using namespace std;

int main() {
    int n;
    cin >> n;

    for (int i =  0; i < n; i++) {
        ll a, b;
        cin >> a >> b;
        bool res;

        if (a == 0 != b == 0) {
            res = false;
        } else {
            bool x =  (2 * a - b) >= 0  && (2 * a - b) % 3 == 0;
            bool y =  (2 * b - a) >= 0  && (2 * b - a) % 3 == 0;
            res = x && y;
        }
        cout << (res ? "YES" : "NO") << endl;;
    }
}
