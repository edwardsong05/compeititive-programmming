# problem on kattis
# https://open.kattis.com/problems/aprizenoonecanwin
# greedy algorithm

n, X = [int(i) for i in input().split()]
prices = [int(i) for i in input().split()]

prices.sort()

last_index = len(prices)-1

for i in reversed(range(1, len(prices))):
    last_index = i
    if prices[i] + prices[i-1] <= X:
        break

if last_index == 1:
    if prices[1] + prices[0] <= X:
        print(2)
    else:
        print(1)
else:
    print(last_index + 1)
