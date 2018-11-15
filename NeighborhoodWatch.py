# problem on kattis

inp = input().split()
N = int(inp[0])
K = int(inp[1])

watches = []
for i in range(K):
    inp = input()
    inp = int(inp) - 1
    watches.append(inp)

total = 0
last = 0
if K == 0:
    pass
else:
    for i in watches:
        total += (N - i) * (i+1-last)
        last = i+1

print(total)
