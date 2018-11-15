# problem on kattis
# greedy algorithm

T = input()
T = int(T)

for j in range(T):
    n = input()
    n = int(n)

    v1 = [int(i) for i in input().split()]
    v2 = [int(i) for i in input().split()]

    v1 = sorted(v1)
    v2 = sorted(v2, reverse=True)

    total = 0

    for i in range(n):
        total += v1[i] * v2[i]

    print('Case #' + str(j+1) + ': ' + str(total))