# for the "Kitten on a Tree" problem on kattis
# using depth first search algorithm
# problem could be adapted to breadth first search by changing the data structure (ds) to a queue
# depth first search uses a stack


# function searches for a path from src to dst, stores path in the path dictionary
def graph_search(src, dst):
    seen = [src]  # this acts like a set containing nodes we have explored
    ds = [src]  # change this to be a queue if we want to use breadth first search

    while len(ds) > 0:  # while we still have nodes to explore
        node = ds.pop()
        if node in graph.keys():  # if this node leads to other nodes
            for neighbour in graph[node]:
                if neighbour == dst:  # if one of the neighbour nodes is dst we stop
                    ds.append(neighbour)
                    path[neighbour] = node  # update the path
                    return
                elif neighbour not in seen:  # if the neighbour node is not in dst we continue searching
                    seen.append(neighbour)
                    ds.append(neighbour)
                    path[neighbour] = node  # update the path


dst = int(input())  # destination
graph = dict()
inp = input().split()
inp = [int(x) for x in inp]
src = inp[0]  # starting point
path = dict()

# build the tree using input
for i in inp:
    path[i] = 0

graph[inp[0]] = inp[1:]

while True:
    inp = input().split()
    inp = [int(x) for x in inp]

    if inp[0] == -1:
        break

    for i in inp:
        path[i] = 0

    graph[inp[0]] = inp[1:]

# search for a path from src to dst
graph_search(src, dst)

# print the result
out = str(dst)
next = dst
while next != src:
    next = path[next]
    out += ' ' + str(next)

print(out)
