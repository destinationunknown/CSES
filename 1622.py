# Creating Strings I
# Given a string, your task is to generate all different strings that can be created using its characters.
# First print an integer k: the number of strings. Then print k lines: the strings in alphabetical order.

s = input()

# Convert s to list of letters
letters = list(s)

# Set to store possible strings
words = set()

# Recursive function to create all possible permutations


def numWays(word, letters):
    # Base case where there is only one possible letter to add, so add the formed word to the set
    if len(letters) == 1:
        words.add(word + letters[0])
    # Loop through all the possible letter additions, then recursively call the function with the remaining letters
    else:
        for i in range(len(letters)):
            numWays(word + letters[i], letters[0:i] + letters[i+1:])


# We start with an empty word and all the characters of the strings as letters
numWays("", letters)

print(len(words))
print("\n".join(sorted(words)))
