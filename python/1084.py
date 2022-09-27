# Apartments
# There are n apartments and m free applicants. Your task is to distrivute the apartments so that as many applicants as possible will get an apartment.
# Each applicant has a desired apartment size, and they will accept any apartment whose size is close enough to the desired size

n, m, k = map(int, input().split())

# Sort at input
desired = list(sorted(map(int, input().split())))
sizes = list(sorted(map(int, input().split())))

# i => position in desired (index of current person)
i = 0
# j => position in sizes (index of current apartment)
j = 0

count = 0

# Stop if we run out of apartments or people
while i < len(desired) and j < len(sizes):
    # If the current apartment and person is a match, add to the count and move to the next person and apartment
    if abs(desired[i] - sizes[j]) <= k:
        i += 1
        j += 1
        count += 1
    else:
        # If the current apartment is too big for the current person, he will never find a match (list is sorted), so move on to the next person
        if sizes[j] > desired[i] + k:
            i += 1
        # Likewise for when the current person wants an apartment bigger than the current one
        else:
            j += 1

print(count)
