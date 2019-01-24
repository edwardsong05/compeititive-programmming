# problem on kattis
# https://open.kattis.com/problems/collatz
# simulation


def step(num):
    if num % 2 == 0:
        return int(num / 2)
    else:
        return int(3 * num + 1)

while True:
    A, B = [int(i) for i in input().split()]

    if A == 0 and B == 0:
        break

    seq1 = A
    seq2 = [B]

    while seq2[-1] != 1:
        seq2.append(step(seq2[-1]))

    steps1 = 0
    steps2 = 0
    match = False

    while True:
        if seq1 in seq2:
            steps2 = seq2.index(seq1)
            break
        else:
            seq1 = step(seq1)
            steps1 += 1

        if seq1 == 1:
            steps2 = len(seq2) - 1
            break

    print("%d needs %d steps, %d needs %d steps, they meet at %d" % (A, steps1, B, steps2, seq2[steps2]))
