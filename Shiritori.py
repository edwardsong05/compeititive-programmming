# problem on kattis
# https://open.kattis.com/problems/shiritori
# simulation

N = int(input())

turn = 1
prev = input()
seen = set()
seen.add(prev)

finished = True

for i in range(N-1):
    line = input()

    if prev[-1] != line[0]:
        print('Player', turn % 2 + 1, 'lost')
        finished = False
        break
    elif line in seen:
        print('Player', turn % 2 + 1, 'lost')
        finished = False
        break

    seen.add(line)
    turn += 1
    prev = line

if finished:
    print('Fair Game')
