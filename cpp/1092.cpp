#include <iostream>
#include <vector>
typedef long long ll;

using namespace std;

int main() {
    ll n;
    cin >> n;

    // If the sum is not even, then it is impossible for two sets to have the same sum
    if (n * (n+1) / 2 % 2) {
        cout << "NO" << endl;
        return 0;
    }

    // Otherwise, the sum of each set will be (n)(n+1)/4
    ll sum = n * (n + 1) / 4;

    vector<ll> a;
    vector<ll> b;

    ll curr = 0;

    for (ll i = n; i > 0; i--) {
        if (curr + i <= sum) {
            a.push_back(i);
            curr += i;
        } else {
            b.push_back(i);
        }
    }

    cout << "YES" << endl;
    cout << a.size() << endl;
    for (ll i : a) {
        cout << i << ' ';
    }
    cout << endl;
    cout << b.size() << endl;
    for (ll i : b) {
        cout << i << ' ';
    }
    cout << endl;
}
