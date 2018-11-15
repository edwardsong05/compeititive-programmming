# for the "Where's My Internet??" Problem on Kattis
# this problem could also be solved using sets but sets can be slow and would likely run out of time
# therefore union find should be implemented

# get number of houses and number of network cables
inp = input()
inp = inp.split()
num_houses = int(inp[0])
num_cables = int(inp[1])

# create an array with the numbers of houses
houses = [x for x in range(num_houses)]

# for the number of network cables get the houses connected and update the array references
for i in range(num_cables):
    inp = input()
    inp = inp.split()
    house1 = int(inp[0]) - 1
    house2 = int(inp[1]) - 1
    
    # navigate to the root first and then add to the tree
    base1 = house1
    base2 = house2

    while houses[base1] != base1:
        base1 = houses[base1]
    while houses[base2] != base2:
        base2 = houses[base2]

    if base1 > base2:
        houses[base1] = houses[base2]
    else:
        houses[base2] = houses[base1]

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