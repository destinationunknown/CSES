# Missing Number
# You are given all numbers between 1,2,…,n except one. Your task is to find the missing number.
n = int(input())
a = set([int(x) for x in input().split()])
b = set([int(x) for x in range(1, n + 1)])

print(next(iter(b-a)))
