# problem on kattis
# https://open.kattis.com/problems/stockbroker
# greedy algorithm

d = int(input())

days = []

for i in range(d):
    days.append(int(input()))

end = d-1

for i in reversed(range(d)):
    if days[i] >= days[end]:
        end = i
    else:
        break

total = 100
stock = 0

for i in range(end):
    if stock == 0:
        if days[i] < days[i+1]:
            if int(total/days[i]) < 100000:
                stock = int(total/days[i])
                total -= stock * days[i]
            else:
                stock = 100000
                total -= stock * days[i]
    else:
        if days[i] > days[i+1]:
            total += stock * days[i]
            stock = 0

total += days[end] * stock

print(total)
