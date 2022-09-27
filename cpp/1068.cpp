#include <iostream>

int main() {
    long long n;
    std::cin >> n;

    while (true) {
        std::cout << n;

        if (n == 1) {
            std::cout << std::endl;
            break;
        }

        if (n % 2) {
            n *= 3;
            n += 1;
        } else {
            n /= 2;
        }

        std::cout << " ";
    }
}
