# DartScoring problem on kattis
# https://open.kattis.com/problems/dartscoring
# convex hull problem

# graham scan algorithm from https://gist.github.com/arthur-e/5cf52962341310f438e96c1f3c3398b8
from functools import reduce


def convex_hull_graham(points):
    TURN_LEFT, TURN_RIGHT, TURN_NONE = (1, -1, 0)

    def cmp(a, b):
        return (a > b) - (a < b)

    def turn(p, q, r):
        return cmp((q[0] - p[0])*(r[1] - p[1]) - (r[0] - p[0])*(q[1] - p[1]), 0)

    def _keep_left(hull, r):
        while len(hull) > 1 and turn(hull[-2], hull[-1], r) != TURN_LEFT:
            hull.pop()
        if not len(hull) or hull[-1] != r:
            hull.append(r)
        return hull

    points.sort(key=lambda x: (x[1], x[0]))
    l = reduce(_keep_left, points, [])
    u = reduce(_keep_left, reversed(points), [])

    return l.extend(u[i] for i in range(1, len(u) - 1)) or l

while True:
    try:
        darts = []
        inp = [float(i) for i in input().split()]

        for i in range(0, len(inp), 2):
            darts.append((inp[i], inp[i+1]))
        num = len(darts)
        hull = convex_hull_graham(darts)

        perm = 0.0
        for i in range(1, len(hull)):
            perm += ((hull[i-1][0] - hull[i][0])**2 + (hull[i-1][1] - hull[i][1])**2)**0.5

        perm += ((hull[-1][0] - hull[0][0])**2 + (hull[-1][1] - hull[0][1])**2)**0.5

        print(100*num/(1+perm))
    except:
        break
