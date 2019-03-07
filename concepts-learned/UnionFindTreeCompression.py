# Where's My Internet?? problem on Kattis
# https://open.kattis.com/problems/wheresmyinternet
# union find with tree compression

# get number of houses and number of network cables
inp = input()
inp = inp.split()
num_houses = int(inp[0])
num_cables = int(inp[1])

# create an array with the numbers of houses
houses = [x for x in range(num_houses)]


# get the root of each set
def root(id):
    while (houses[id] != id):
        houses[id] = houses[houses[id]]  # tree compression
        id = houses[id]
    return id


# join the two sets on the smaller number
def union(id1, id2):
    p = root(id1)
    q = root(id2)
    if p < q:
        houses[q] = houses[p]
    else:
        houses[p] = houses[q]


# for the number of network cables get the houses connected and update the array references
for i in range(num_cables):
    inp = input()
    inp = inp.split()
    house1 = int(inp[0]) - 1
    house2 = int(inp[1]) - 1

    # navigate to the root first and then add to the tree
    union(house1, house2)

# check each house, if the root is connected to house 1
check = True
for i in range(num_houses):
    house_num = i
    if houses[i] != i and houses[i] != 0:
        # store the original house away
        house_num = i
        i = houses[i]
        # if the number stored in the array refers to another house
        # traverse elements until we reach the smallest house of the set
        while houses[i] != i and i != 0:
            i = houses[i]
    if houses[i] != 0:
        print(house_num + 1)
        check = False

if check:
    print('Connected')
