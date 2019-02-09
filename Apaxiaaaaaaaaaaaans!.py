# problem on kattis
# https://open.kattis.com/problems/apaxiaaans
# simulation

inp = input()
last = None

for i in inp:
    if last != i:
        print(i, end='')
        last = i
    else:
        last = i
