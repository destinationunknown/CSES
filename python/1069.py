# Repetitions
# You are given a DNA sequence: a string consisting of characters A, C, G, and T. Your task is to find the longest repetition in the sequence. This is a maximum-length substring containing only one type of character.

s = input()

cur = ""
cnt = 0
max_cnt = 0

# Find the length of each sequence of repeating characters, and check if it is longer than the max each time a new one is found

for char in s:
    if char == cur:
        cnt += 1
    else:
        max_cnt = max(cnt, max_cnt)
        cnt = 1
        cur = char

max_cnt = max(cnt, max_cnt)

print(max_cnt)
