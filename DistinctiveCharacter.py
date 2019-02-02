# problem on kattis
# https://open.kattis.com/problems/distinctivecharacter
# breadth first search, bitwise

from collections import deque


def search(k):
    last = None

    while bfs:
        node = bfs.popleft()

        last = node

        for i in range(k):
            new_node = node ^ 1 << i

            if new_node not in seen:
                bfs.append(new_node)
                seen.add(new_node)

    return last


inp = raw_input().split()
n = int(inp[0])
k = int(inp[1])


bfs = deque()
seen = set()

for i in range(n):
    player = int(raw_input(), 2)
    bfs.append(player)
    seen.add(player)

ans = bin(search(k))[2:]

print(ans.zfill(k))
