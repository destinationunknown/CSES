#include <iostream>
typedef long long ll;

using namespace std;

ll pow(ll base, ll exp, ll mod) {
    ll res = 1;
    while (exp > 0) {
        if (exp % 2) {
            res = (res * base) % mod;
        }

        exp = exp >> 1;
        base = (base * base ) % mod;
    }

    return res;
}

int main() {
    ll n;
    cin >> n;

    ll res = pow(2, n, 1000000007);
    cout << res << endl;
}
