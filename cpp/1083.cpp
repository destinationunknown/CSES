#include <iostream>

int main() {
    long long n;
    std::cin >> n;

    long long sum = 0;
    long long d;

    for (long long i = 0; i < n - 1; i++) {
        std::cin >> d;
        sum += d;
    }

    long long expected_sum = (n * (n + 1)) / 2;
    long long result = expected_sum - sum;

    std::cout << result << std::endl;
}
