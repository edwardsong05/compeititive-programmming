# problem on kattis
# https://open.kattis.com/problems/cold
# simulation

n = int(input())
inp = input().split()
out = 0

for temp in inp:
    if int(temp) < 0:
        out += 1

print(out)
