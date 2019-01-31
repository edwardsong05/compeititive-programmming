# problem on kattis
# https://open.kattis.com/problems/onechicken
# simulation

N, M = [int(i) for i in input().split()]

if M-N > 1:
    print("Dr. Chaz will have", M-N, "pieces of chicken left over!")
elif M-N > 0:
    print("Dr. Chaz will have", M-N, "piece of chicken left over!")
elif N-M == 1:
    print("Dr. Chaz needs", N-M, "more piece of chicken!")
else:
    print("Dr. Chaz needs", N-M, "more pieces of chicken!")
