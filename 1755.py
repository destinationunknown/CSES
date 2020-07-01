# Palindrome Reorder
# Given a string, your task is to reorder its letters in such a way that it becomes a palindrome (i.e., it reads the same forwards and backwards).
# If there are no solutions, print "NO SOLUTION"


s = input()

# Loop through the array and keep track of which characters have a pair and which are single (have no pair)
pairs = []
single = []

for char in s:
    if char in single:
        single.remove(char)
        pairs.append(char)
    else:
        single.append(char)

# Construct the palindrome by sandwiching the single elements between the pair elements
res = ''.join(pairs) + ''.join(single) + ''.join(pairs)[::-1]

# Check if it is a palindrome
if res == res[::-1]:
    print(res)
else:
    print("NO SOLUTION")
