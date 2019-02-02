# problem on kattis
# https://open.kattis.com/problems/flexible
# simulation

W, P = [int(i) for i in input().split()]
L = [int(i) for i in input().split()]

options = []

options.append(W)

if P >= 1:
    for i in L:
        if i not in options:
            options.append(i)
        if W-i not in options:
            options.append(W-i)
if P >= 2:
    for i in range(len(L) - 1):
        for j in range(i+1, len(L)):
            if L[j] - L[i] not in options:
                options.append(L[j] - L[i])

options.sort()

for i in options:
    print(i, end=' ')
