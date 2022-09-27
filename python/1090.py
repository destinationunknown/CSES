# Ferris Wheel
# There are n children who want to go to a Ferris wheel, and your task is to find a gondola for each child.
# Each gondola may have one or two children in it, and in addition, the total weight in a gondola may not exceed x.
# You know the weight of each child.
# What is the minimum number of gondolas needed?

n, x = map(int, input().split())

# Sort weights at input
weights = list(sorted(map(int, input().split())))

count = 0

# Use a two pointer approach. i is the index of the lightest available person, while j is the index of the heaviest
i = 0
j = len(weights) - 1

# We have run out of people when i > j
while i <= j:
    # Check if the current combination is too heavy
    if weights[i] + weights[j] > x:
        # If it is, then create a gondola with only the child at j
        count += 1
        j -= 1
    else:
        # If not, use both children at this gondola
        count += 1
        j -= 1
        i += 1


print(count)
