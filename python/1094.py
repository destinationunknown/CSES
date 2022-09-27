# Increasing Array
# You are given an array of n integers. You want to modify the array so that it is increasing, i.e., every element is at least as large as the previous element.
# On each turn, you may increase the value of any element by one. What is the minimum number of turns required?

n = int(input())

arr = [int(x) for x in input().split(' ')]

count = 0

# Track the number of times each element must be increased
for i in range(1, n):
    increase = 0
    if arr[i] < arr[i-1]:
        increase = arr[i-1] - arr[i]
        arr[i] += increase
        count += increase
