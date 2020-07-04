# Apple Division
# There are n apples with known weights. Your task is to divide the apples into two groups so that the difference between the weights of the groups is minimal.

n = int(input())

weights = list(map(int, input().split()))


# Recursive function to find the minimum difference
# index = the index of the current weight
# a, b = the sums of sets a and b
def min_difference(index, a, b):

    # Handle base case, find the difference of the sums
    if index >= len(weights):
        return abs(a - b)

    # Try adding the weight at the index to either set a or set b, and find the outcome with minimum sum
    return min(min_difference(index + 1, a + weights[index], b), min_difference(index + 1, a, b + weights[index]))


# We start with the first weight, so index = 0
# Sets a and b are initially empty, a, b = 0
print(min_difference(0, 0, 0))
