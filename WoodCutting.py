# problem on kattis
# https://open.kattis.com/problems/woodcutting
# greedy algorithm

T = int(input())

for i in range(T):
    N = int(input())
    wood = []
    time = 0
    waiting = 0

    for j in range(N):
        temp = [int(i) for i in input().split()]
        wood.append(sum(temp[1:]))

    wood.sort()
    for j in wood:
        time += j + waiting
        waiting += j

    print(time/N)
