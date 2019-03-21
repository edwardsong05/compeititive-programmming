# problem on kattis
# https://open.kattis.com/problems/recount
# simulation

counts = dict()

while True:
    inp = input()

    if inp == '***':
        break

    if inp in counts.keys():
        counts[inp] += 1
    else:
        counts[inp] = 1

max_count = 0
person = None
split = False

for i, j in counts.items():
    if j > max_count:
        person = i
        max_count = j
        split = False
    elif max_count == j:
        split = True

if not split:
    print(person)
else:
    print('Runoff!')
