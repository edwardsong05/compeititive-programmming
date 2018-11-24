# problem on CodeForces, contest ID: 1061
# https://codeforces.com/problemset/problem/1061/B
# greedy algorithm

inp = input().split()
n = int(inp[0])
m = int(inp[1])
a = [int(i) for i in input().split()]
a.sort(reverse=True)

remove = 0
height = 0

for i in range(len(a)):
    if i == 0:
        height = a[i]
    elif a[i] == 1:
        if height == 1:
            break
        else:
            remove += 1
            break
    else:
        diff = a[i-1] - a[i]
        if diff != 0:
            if height > a[i]:
                remove += a[i]
                height = a[i]
            elif height == a[i]:
                remove += a[i]
                height -= 1
            else:
                if height == 1:
                    remove += a[i] - 1
                else:
                    remove += a[i]
                    height -= 1
        else:
            if height > 1:
                remove += a[i]
                height -= 1
            else:
                remove += a[i]-1

print(remove)

