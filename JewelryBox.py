# problem on kattis
# https://open.kattis.com/problems/jewelrybox
# ternary search


def volume(x, y, h):
    return (x-2*h)*(y-2*h)*h


T = int(input())

for i in range(T):
    x, y = [int(i) for i in input().split()]

    left = 0
    right = min([x, y]) / 2

    while right-left > 10**-6:
        m1 = left + (right - left) / 3
        m2 = right - (right - left) / 3
        v1 = volume(x, y, m1)
        v2 = volume(x, y, m2)
        if v1 > v2:
            right = m2
        else:
            left = m1
    print(volume(x, y, left))
