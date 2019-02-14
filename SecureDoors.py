# problem on kattis
# https://open.kattis.com/problems/securedoors
# simulation

n = int(input())

persons = dict()

for i in range(n):
    inp = input().split()

    if inp[0] == 'entry':
        if inp[1] in persons.keys():
            if persons[inp[1]] == 'entry':
                print(inp[1], 'entered (ANOMALY)')
            else:
                print(inp[1], 'entered')
                persons[inp[1]] = 'entry'
        else:
            persons[inp[1]] = 'entry'
            print(inp[1], 'entered')
    else:
        if inp[1] in persons.keys():
            if persons[inp[1]] == 'exit':
                print(inp[1], 'exited (ANOMALY)')
            else:
                print(inp[1], 'exited')
                persons[inp[1]] = 'exit'
        else:
            print(inp[1], 'exited (ANOMALY)')
