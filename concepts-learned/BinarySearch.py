# problem on kattis
# https://open.kattis.com/problems/ballotboxes
# binary search

from math import ceil

while True:
    N, B = [int(i) for i in input().split()]

    if N == -1 and B == -1:
        break

    pop = []
    max_val = 0
    min_val = 0

    for i in range(N):
        inp = int(input())
        pop.append(inp)

        if inp > max_val:
            max_val = inp

    input()

    # apply binary search
    while (min_val < max_val):
        mid = int((max_val + min_val) / 2)

        boxes = 0
        for i in pop:
            boxes += ceil(i / mid)

        if boxes <= B:
            max_val = mid
        else:
            min_val = mid + 1

    print(min_val)
