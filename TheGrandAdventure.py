# problem on kattis
# https://open.kattis.com/problems/thegrandadventure
# simulation, stack

from collections import deque

n = int(input())

for i in range(n):
    inp = input()
    backpack = deque()
    possible = True

    for j in inp:
        if j == '$' or j == '|' or j == '*':
            backpack.append(j)
        elif j == 't':
            if len(backpack) == 0:
                possible = False
                break
            else:
                item = backpack.pop()
                if item != '|':
                    possible = False
                    break
        elif j == 'j':
            if len(backpack) == 0:
                possible = False
                break
            else:
                item = backpack.pop()
                if item != '*':
                    possible = False
                    break
        elif j == 'b':
            if len(backpack) == 0:
                possible = False
                break
            else:
                item = backpack.pop()
                if item != '$':
                    possible = False
                    break

    if possible and len(backpack) == 0:
        print('YES')
    else:
        print('NO')
