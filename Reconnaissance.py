# problem on kattis
# https://open.kattis.com/problems/reconnaissance
# ternary search


def distance(time):
    min_dis = max_dis = pos[0] + (time*vel[0])
    for i in range(len(pos)):
        temp = pos[i] + (time*vel[i])

        if temp < min_dis:
            min_dis = temp
        elif temp > max_dis:
            max_dis = temp

    return max_dis - min_dis

n = int(raw_input())

pos = []
vel = []

for i in range(n):
    x, v = map(int, raw_input().split())
    pos.append(x)
    vel.append(v)

# perfrom ternary search on time
left = 0
right = 200001  # starting value

while right-left > 10**-7:
    m1 = left + (right - left) / 3.0
    m2 = right - (right - left) / 3.0
    dist1 = distance(m1)
    dist2 = distance(m2)

    if dist1 < dist2:
        right = m2
    else:
        left = m1

print(distance(left))
