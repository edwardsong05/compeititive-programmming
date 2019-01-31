# problem on kattis
# https://open.kattis.com/problems/bitbybit
# simulation, bitwise

while True:
    n = int(input())

    if n == 0:
            break

    num = ['?']*32

    for i in range(n):
        inp = input().split()

        if inp[0] == "CLEAR":
            num[int(inp[1])] = 0

        elif inp[0] == "SET":
            num[int(inp[1])] = 1

        elif inp[0] == "OR":
            temp1 = num[int(inp[1])]
            temp2 = num[int(inp[2])]
            if temp1 == 1 or temp2 == 1:
                num[int(inp[1])] = 1
            elif temp1 == '?' or temp2 == '?':
                num[int(inp[1])] = '?'

        else:
            temp1 = num[int(inp[1])]
            temp2 = num[int(inp[2])]
            if temp1 == '?' or temp2 == '?':
                if temp1 == 0 or temp2 == 0:
                    num[int(inp[1])] = 0
                else:
                    num[int(inp[1])] = '?'
            else:
                num[int(inp[1])] = temp1 * temp2

    for i in reversed(num):
        print(i, end='')
    print()
