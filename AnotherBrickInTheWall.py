# problem on kattis
# https://open.kattis.com/problems/anotherbrick
# simulation

h, w, n = [int(i) for i in input().split()]
bricks = [int(i) for i in input().split()]

length = 0
height = 0
finished = False

for brick in bricks:
    length += brick

    if length == w:
        length = 0
        height += 1

        if height == h:
            finished = True
            break

    if length > w:
        break

if finished:
    print('YES')
else:
    print('NO')
