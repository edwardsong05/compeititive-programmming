# problem on kattis
# https://open.kattis.com/problems/threepowers
# binary represents subsets

while True:
    inp = int(input()) - 1

    if inp == -1:
        break

    bin = '{0:b}'.format(inp)

    subset = []

    n = len(bin) - 1
    for i in range(len(bin)):
        if int(bin[n-i]) == 1:
            subset.append(3**i)

    if len(subset) > 0:
        print('{', subset[0], end='')

        for i in range(1, len(subset)):
            print(',', subset[i], end='')

        print(' }')
    else:
        print('{ }')
