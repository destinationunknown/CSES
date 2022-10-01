#include <iostream>

typedef long long ll;

int main() {
    ll n;
    std::cin >> n;

    if (n == 1) {
        std::cout << 1 << std::endl;
    }

    if (n <= 3) {
        std::cout << "NO SOLUTION" << std::endl;
    } else {
        int d = n % 2;
        for (int i = n + d - 1; i > 0; i -= 2) {
            std::cout << i << " ";
        }
        for (int i = n - d; i > 0; i -= 2) {
            std::cout << i;
            if (i > 2) {
                std::cout << " ";
            } else {
                std::cout << std::endl;
            }
        }
    }
}
