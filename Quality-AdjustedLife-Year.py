# problem on kattis

n = int(input())

total = 0
for i in range(n):
    inp = input().split()
    total += float(inp[0]) * float(inp[1])

print(total)