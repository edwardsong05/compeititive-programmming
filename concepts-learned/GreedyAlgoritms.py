# using "Bank Queue" problem on kattis
# using a greedy algorithm where for each step we take the locally best solution
# in this case the local best is the largest possible amount of money for the time slot
# but since people can only fit into certain time slots we want to start from the largest
# time slot and move backwards to the smallest time slot

# this ensures we don't exclude people (which would happen if we did using ascending time slot order)
# ie. people: 2000 1 and 1800 0, and 2 time slots 0 and 1
# if we did ascending time slot order and filled based on money
# time slot 0: 2000 1
# time slot 1: 0
# we would have neglected 1800 0 using this method
# max money: 2000

# if we did descending time slot order and filled based on money
# time slot 1: 2000 1
# time slot 0: 1800 0
# we included 1800 0 using this method
# max money: 3800

# get information on the amount of people and time slots
inp = input().split()
N = int(inp[0])
T = int(inp[1])

# get information about the people
people = []
for i in range(N):
    inp = input().split()
    people.append((int(inp[0]), int(inp[1])))

# sort the people based on the amount of money they have
people.sort(key=lambda x: x[0], reverse=True)

# create an array for the time slots we have
serve = [0 for i in range(T)]

# starting from the furthest time slot move to the first time slot
for i in reversed(range(T)):
    # find the largest possible value to insert into the time slot
    for j in range(len(people)):
        if people[j][1] >= i:
            serve[i] = people[j][0]
            people.remove(people[j])
            break

# print the maximum amount of money
print(sum(serve))
