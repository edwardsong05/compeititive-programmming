# problem on kattis
# https://open.kattis.com/problems/conundrum
# simulation

inp = input()

days = 0

for i in range(len(inp)):
    temp = i % 3

    if temp == 0:
        if inp[i] != 'P':
            days += 1
    elif temp == 1:
        if inp[i] != 'E':
            days += 1
    else:
        if inp[i] != 'R':
            days += 1

print(days)
