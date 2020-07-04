# Bit Strings
# Your task is to calculate the number of bit strings of length n.
# For example, if n=3, the correct answer is 8, because the possible bit strings are 000, 001, 010, 011, 100, 101, 110, and 111.
# Print the result modulo 10^9+7.

n = int(input())

# Simple permutation, each digit has 2 possible values (0 and 1) and there are n digits
# The third argument to pow() is the modulus
print(pow(2, n, 10**9 + 7))
