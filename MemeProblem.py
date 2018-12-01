# problem on codeforces
# https://codeforces.com/problemset/problem/1076/C
# iterative math

t = int(input())

for i in range(t):

    d = int(input())

    if d == 0:
        print('Y', 0, 0)
    elif d == 1:
        print('N')
    elif d == 2:
        print('N')
    elif d == 3:
        print('N')
    else:
        a = 3 * d / 4  # initial guess
        b = d/a

        while True:
            if abs(a + b - a * b) < 10**-6 and abs(a + b - d) < 10**-6:
                break
            else:
                a = d - (d / a)
                b = d / a

        print('Y', a, b)
