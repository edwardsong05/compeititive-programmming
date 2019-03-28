# problem on kattis
# https://open.kattis.com/problems/boundingrobots
# simulation

while True:
    w, l = [int(i) for i in input().split()]

    if w == 0 and l == 0:
        break

    x_actual = 0
    y_actual = 0
    x_robo = 0
    y_robo = 0

    n = int(input())

    for i in range(n):
        move, steps = input().split()
        steps = int(steps)

        if move == 'u':
            y_robo += steps
            if steps + y_actual >= l:
                y_actual = l - 1
            else:
                y_actual += steps
        elif move == 'd':
            y_robo -= steps
            if y_actual - steps <= 0:
                y_actual = 0
            else:
                y_actual -= steps
        elif move == 'l':
            x_robo -= steps
            if x_actual - steps <= 0:
                x_actual = 0
            else:
                x_actual -= steps
        else:
            x_robo += steps
            if steps + x_actual >= w:
                x_actual = w - 1
            else:
                x_actual += steps

    print('Robot thinks', x_robo, y_robo)
    print('Actually at', x_actual, y_actual)
    print()
