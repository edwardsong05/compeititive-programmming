# problem on codeforces
# https://codeforces.com/problemset/problem/1082/B
# greedy algorithm

n = int(input())
inp = list(input())

total_g = 0
total_s = 0
number_g = 0

arr = []

for i in range(len(inp)):
    if inp[i] == 'G':
        if total_s > 0:
            arr.append(-total_s)
            total_s = 0
        total_g += 1
    else:
        if total_g > 0:
            arr.append(total_g)
            total_g = 0
            number_g += 1
        total_s += 1

if total_s > 0:
    arr.append(-total_s)
else:
    arr.append(total_g)
    number_g += 1

first = 0
second = 0
longest = 0
last = 0

for j in range(len(arr)):
    if arr[j] > 0:
        break

if arr[j] > 0 and number_g >= 2:
    longest = arr[j] + 1
    first = arr[j]
elif arr[j] > 0:
    longest = arr[j]
    first = arr[j]

for i in range(j+1, len(arr)):
    if arr[i] > 0:
        second = arr[i]
        if last == -1:
            temp = second + first
            if number_g == 2:
                if temp > longest:
                    longest = temp
            else:
                if temp+1 > longest:
                    longest = temp+1
        else:
            if number_g >= 2:
                if second+1 > longest:
                    longest = second + 1
            elif second > longest:
                longest = second

        first = second

    else:
        last = arr[i]

print(longest)
