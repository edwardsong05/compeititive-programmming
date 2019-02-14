# problem on kattis
# https://open.kattis.com/contests/nu6ia8/problems/incognito
# simulation

tests = int(input())

for i in range(tests):
    n = int(input())
    attributes = dict()
    for i in range(n):
        inp = input().split()

        if inp[1] in attributes.keys():
            attributes[inp[1]] += 1
        else:
            attributes[inp[1]] = 1

    combos = 1
    for val in attributes.values():
        combos *= (val+1)
    combos -= 1

    print(combos)
