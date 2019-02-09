# problem on kattis
# https://open.kattis.com/problems/fruitbaskets
# binary represents subsets

N = int(input())
weights = [int(i) for i in input().split()]
weights.sort()

total = 0
break_point = 0

# find where 200 or greater exists
for i in range(len(weights)):
    break_point = i

    if weights[i] >= 200:
        break

local_max = '1' * (break_point + 1)

# add up values till local maximum value of fruits
for i in range(int(local_max, 2) + 1):
    basket = bin(i)[2:]
    basket_total = 0

    for j in reversed(range(len(basket))):
        if basket[j] == '1':
            basket_total += weights[len(basket) - 1 - j]

    if basket_total >= 200:
        total += basket_total

# calculate fruit weights from local max to heaviest fruit (maximum)
for i in range(len(local_max), len(weights)):
    num = int('1' * (i+1), 2) - int('1' * i, 2)
    total += weights[i] * num

    for j in range(i):
        total += int(weights[j] * (num / 2))

print(total)
