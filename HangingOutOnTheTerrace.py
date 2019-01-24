# problem on kattis
# https://open.kattis.com/problems/hangingout
# simulation

inp = input().split()
L = int(inp[0])
x = int(inp[1])

total = 0
denied = 0

for i in range(x):
    inp = input().split()
    p = int(inp[1])

    if inp[0] == 'enter':
        if L < total + p:
            denied += 1
        else:
            total += p
    else:
        total -= p

print(denied)
