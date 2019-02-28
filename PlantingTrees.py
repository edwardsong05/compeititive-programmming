# problem on kattis
# https://open.kattis.com/problems/plantingtrees
# greedy algorithm

N = int(input())
trees = [int(i) for i in input().split()]
trees.sort(reverse=True)

current_day = 0
day_mature = 1

for t in trees:
    if current_day + t > day_mature:
        day_mature = current_day + t
    current_day += 1

print(day_mature+2)
