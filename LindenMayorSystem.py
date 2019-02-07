# problem on kattis
# https://open.kattis.com/problems/lindenmayorsystem
# simulation

n, m = [int(i) for i in input().split()]

rules = dict()

for i in range(n):
    inp = input().split()
    rules[inp[0]] = inp[2]

seq = input()

for i in range(m):
    temp = ''
    for letter in seq:
        if letter in rules.keys():
            temp += rules[letter]
        else:
            temp += letter

    seq = temp

print(seq)
