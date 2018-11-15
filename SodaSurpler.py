# problem on kattis

inp = input()
inp = inp.split()

drinks = 0
bottles = int(inp[0]) + int(inp[1])
cost = int(inp[2])

while bottles >= cost:
    drinks += 1
    bottles += 1
    bottles -= cost

print(drinks)

