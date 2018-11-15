# problem on kattis
# greedy algorithm

inp = input().split()
Q = int(inp[0])
M = int(inp[1])
S = int(inp[2])
L = int(inp[3])

big = int(L / M)
remainder = L % M

if remainder > 0:
    max_t = big * Q + Q
    remaining_machines = M - remainder
    if S / remaining_machines > Q:
        remaining_s = S - (remaining_machines*Q)
        max_t += int(remaining_s/M)
        if remaining_s % M > 0:
            max_t += 1
else:
    max_t = big * Q
    max_t += int(S/M)
    if S % M > 0:
        max_t += 1

print(max_t)
