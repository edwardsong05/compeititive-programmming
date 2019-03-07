# problem on kattis
# https://open.kattis.com/problems/battlesimulation
# simulation

inp = input()

moves = {'R': 'S', 'B': 'K', 'L': 'H'}
combo = False
skip = 0

if len(inp) >= 3:
    check = [0, 0, 0]
    for i in range(2, len(inp)):
        if skip > 0:
            combo = False
            skip -= 1
            continue

        check[0] = inp[i-2]
        check[1] = inp[i-1]
        check[2] = inp[i]

        if 'R' in check and 'B' in check and 'L' in check:
            print('C', end='')
            i += 2
            combo = True
            skip = 2
        else:
            print(moves[inp[i-2]], end='')
            combo = False
    if not combo:
        for i in range(len(inp)-2, len(inp)):
            if skip > 0:
                skip -= 1
                continue
            print(moves[inp[i]], end='')
else:
    for i in inp:
        print(moves[i], end='')
print()
