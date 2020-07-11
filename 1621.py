# Distinct Numbers
# You are given a list of n integers, and your task is to calculate the number if distinct values in the list

n = int(input())
nums = map(int, input().split())

print(len(set(nums)))
