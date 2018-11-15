# problem on kattis

inp = input().split()
m = int(inp[0])
n = int(inp[1])

def delete_circle(i, j):
    picture[i][j] = '.'
    if j+1 < n and picture[i][j+1] == '#':
        delete_circle(i, j+1)
    if i+1 < m and picture[i+1][j] == '#':
        delete_circle(i+1, j)
    if j-1 >= 0 and picture[i][j-1] == '#':
        delete_circle(i, j-1)
    if i-1 >= 0 and picture[i-1][j] == '#':
        delete_circle(i-1, j)
    if j+1 < n and i+1 < m and picture[i+1][j+1] == '#':
        delete_circle(i+1, j+1)
    if j+1 < n and i-1 >= 0 and picture[i-1][j+1] == '#':
        delete_circle(i-1, j+1)
    if j-1 >= 0 and i+1 < m and picture[i+1][j-1] == '#':
        delete_circle(i+1, j-1)
    if j-1 >= 0 and i-1 >= 0 and picture[i-1][j-1] == '#':
        delete_circle(i-1, j-1)


count = 0
picture = []
for i in range(m):
    inp = input()
    inp = [x for x in inp]
    picture.append(inp)

for i in range(m):
    for j in range(n):
        if picture[i][j] == '#':
            delete_circle(i, j)
            count += 1
print(count)
