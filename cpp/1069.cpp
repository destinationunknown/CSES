#include <algorithm>
#include <iostream>

typedef long long ll;

int main() {
    std::string s;
    std::cin >> s;

    ll n = s.length();

    char current;
    char prev = ' ';

    long long int current_streak = 1;
    long long int longest_streak = 1;

    for (ll i = 0; i < n; i++) {
        current = s[i];

        if (current == prev) {
            current_streak += 1;
        } else {
            longest_streak = std::max(current_streak, longest_streak);
            current_streak = 1;
        }

        prev = current;
    }

    longest_streak = std::max(current_streak, longest_streak);

    std::cout << longest_streak << std::endl;
}
