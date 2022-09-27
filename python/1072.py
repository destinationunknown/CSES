# Two Knights
# Your task is to count for k=1,2,…,n the number of ways two knights can be placed on a k×k chessboard so that they do not attack each other.

import operator as op
from functools import reduce


def ncr(n, r):
    r = min(r, n-r)
    numer = reduce(op.mul, range(n, n-r, -1), 1)
    denom = reduce(op.mul, range(1, r+1), 1)
    return numer // denom


n = int(input())

print(0)

for k in range(2, n+1):
    ans = ncr(k ** 2, 2) - 4 * (k-1) * (k-2)
    print(ans)
