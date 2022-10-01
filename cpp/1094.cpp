#include <iostream>

typedef long long ll;

int main() {
    ll n;
    std::cin >> n;

    ll current;
    ll prev;
    ll diff;
    ll sum = 0;

    std::cin >> prev;

    for (int i = 1; i < n; i++) {
        std::cin >> current;
        if (current < prev) {
            diff = prev - current;
            sum += diff;
            current += diff;
        }

        prev = current;
    }

    std::cout << sum << std::endl;
}
