# problem on kattis
# https://open.kattis.com/problems/sok
# simulation

A, B, C = [int(i) for i in input().split()]
I, J, K = [int(i) for i in input().split()]

max_drinks = [A/I, B/J, C/K]

smallest = min(max_drinks)

print(A-I*smallest, B-J*smallest, C-K*smallest)
