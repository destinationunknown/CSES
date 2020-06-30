# Coin Piles
# You have two coin piles containing a and b coins. On each move, you can either remove one coin from the left pile and two coins from the right pile, or two coins from the left pile and one coin from the right pile.

# Your task is to efficiently find out if you can empty both the piles.

t = int(input())

for i in range(t):
    a, b = map(int, input().split())

    # Ensure a > b
    if a < b:
        a, b = b, a

    # If a > 2b, then even if we remove 2 from a each time there will be some remaining after b = 0
    if a > 2 * b:
        print("NO")

    # Let x be the number of times we take 2 from a and 1 from b
    # Let y be the number of times we take 1 from a and 2 from b
    # We can write this as:
    # a = 2x + y
    # b = 2y + x
    #
    # Solving for x and y we get:
    # 3x = 2a - b
    # 3y = 2b - a
    #
    # Since x + y must be a positive integer, a + b must be divisible by 3
    elif (a + b) % 3 == 0:
        print("YES")
    else:
        print("NO")
