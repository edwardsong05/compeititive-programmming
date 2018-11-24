# problem on CodeForces, contest ID: 1061
# https://codeforces.com/problemset/problem/1061/A
# greedy algorithm

inp = input().split()

n = int(inp[0])
S = int(inp[1])

total = 0
counter = 0

while total != S:
    if S-total > n:
        total += n
        counter += 1
    else:
        total += S-total
        counter += 1

print(counter)
