# problem on kattis
# https://open.kattis.com/problems/pizza2
# simulation

R, C = [int(i) for i in input().split()]

print((R-C)**2/(R**2)*100)
