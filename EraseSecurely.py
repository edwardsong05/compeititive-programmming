# problem on kattis
# https://open.kattis.com/problems/erase
# simulation

N = int(input()) % 2

line1 = input()
line2 = input()

succeed = True

for i in range(len(line1)):
    if N == 1:
        if line1[i] == line2[i]:
            succeed = False
            break
    else:
        if line1[i] != line2[i]:
            succeed = False
            break

if succeed:
    print('Deletion succeeded')
else:
    print('Deletion failed')
