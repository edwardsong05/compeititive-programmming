# problem on kattis
# https://open.kattis.com/problems/owlandfox
# simulation


def sumDigits(n):
    sum = 0

    while n > 0:
        sum += n % 10
        n = n // 10

    return sum

T = int(input())

for i in range(T):
    N = int(input())

    sum = sumDigits(N)
    sum -= 1

    for i in reversed(range(N)):
        if (sum == sumDigits(i)):
            print(i)
            break
