# problem on kattis
# https://open.kattis.com/contests/vppiwv/problems/touchscreenkeyboard
# simulation

t = int(input())

keyboard = dict()

for i in list('qwertyuiop'):
    keyboard[i] = 0

for i in list('asdfghjkl'):
    keyboard[i] = 1

for i in list('zxcvbnm'):
    keyboard[i] = 2

rows = [list('qwertyuiop'), list('asdfghjkl'), list('zxcvbnm')]


def calc_distance(incorrect, correct):
    distance = 0

    for i, j in zip(list(incorrect), list(correct)):
        if i == j:
            continue
        else:
            row_i = keyboard[i]
            row_j = keyboard[j]

            distance += abs(row_i - row_j)  # add the distance between rows

            row_i = rows[row_i].index(i)
            row_j = rows[row_j].index(j)
            distance += abs(row_i - row_j)  # add the distance between columns

    return distance


for i in range(t):
    inp = input().split()
    incorrect = inp[0]
    l = int(inp[1])

    words = []
    for j in range(l):
        inp = input()
        words.append((inp, calc_distance(incorrect, inp)))

    words.sort(key=lambda x: (x[1], x[0]))

    for i in words:
        print(i[0], i[1])
