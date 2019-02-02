# problem on kattis
# https://open.kattis.com/problems/bits
# binary, simulation

T = int(input())

for i in range(T):
    inp = input()
    current = ''
    max_1 = 0

    for j in range(len(inp)):
        current += inp[j]
        temp = bin(int(current)).count('1')

        if temp > max_1:
            max_1 = temp

    print(max_1)
