# problem on kattis
# https://open.kattis.com/contests/n5dypb/problems/leftbeehind
# simulation

while True:
    x, y = [int(i) for i in input().split()]

    if x == 0 and y == 0:
        break

    if x + y == 13:
        print("Never speak again.")

    elif x > y:
        print("To the convention.")

    elif x < y:
        print("Left beehind.")

    elif x == y:
        print("Undecided.")
