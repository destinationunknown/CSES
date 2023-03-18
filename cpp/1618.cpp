#include <iostream>
#include <cmath>
typedef long long ll;

using namespace std;

int main() {

    int n;
    cin >> n;

    int currentPow = 5;

    int res = 0;
    while (currentPow <= n) {
        res += n / currentPow;
        currentPow *= 5;
    }

    cout << res << endl;
}
