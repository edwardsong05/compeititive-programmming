# problem on kattis
# https://open.kattis.com/problems/beehives
# simulation


while True:
    inp = input().split()
    d = float(inp[0])
    N = int(inp[1])

    if d == 0.0 and N == 0:
        break

    hives = []

    for i in range(N):
        j, k = [float(i) for i in input().split()]
        hives.append((j, k))

    sour = set()
    for i in range(len(hives)):
        for j in range(i+1, len(hives)):
            dist = ((hives[i][0] - hives[j][0])**2 + (hives[i][1] - hives[j][1])**2)**0.5

            if dist <= d:
                sour.add(i)
                sour.add(j)

    print(len(sour), 'sour,', N-len(sour), 'sweet')
