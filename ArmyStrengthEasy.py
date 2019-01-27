# problem on kattis
# https://open.kattis.com/contests/vppiwv/problems/armystrengtheasy
# greedy algorithm

T = int(input())

for i in range(T):
    inp = input()
    N_G, N_M = [int(i) for i in input().split()]

    godzilla = [int(i) for i in input().split()]
    mecha = [int(i) for i in input().split()]
    godzilla.sort()
    mecha.sort()

    while N_G > 0 and N_M > 0:
        if godzilla[0] < mecha[0]:
            N_G -= 1
            godzilla.remove(godzilla[0])
        elif mecha[0] < godzilla[0]:
            N_M -= 1
            mecha.remove(mecha[0])
        else:
            N_M -= 1
            mecha.remove(mecha[0])

    if N_G == 0:
        print('MechaGodzilla')
    else:
        print('Godzilla')
