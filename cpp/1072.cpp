#include <iostream>
typedef long long ll;

using namespace std;

int main() {
    ll n;
    std::cin >> n;

    for (ll k = 1; k <= n; k++) {
        // On a k*k chessboard, there are k*k spots for the first knight and k*k -1 spots for the second knight
        // Since the knights are indistinguishable, swapping their positions does not change anything, so we need to remove duplicates
        ll total = (k*k)*(k*k -1)/2;

        // Any "invalid" position has the two knights contained in a 2x3 block
        // There are 2 possible orientations of the 2x3 block
        // We also have to account for duplicate cases
        ll invalid = (k - 1)*(k - 2) * 4;

        ll res = total - invalid;
        cout << res << endl;
    }
}
