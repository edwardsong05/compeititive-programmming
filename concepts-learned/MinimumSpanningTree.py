# Artic Network Problem on kattis
# https://open.kattis.com/problems/arcticnetwork
# minimum spanning tree
# algorithm adapted from https://www.hackerearth.com/practice/algorithms/graphs/minimum-spanning-tree/tutorial/


def distance(point1, point2):
    return ((point1[0] - point2[0])**2 + (point1[1] - point2[1])**2)**(0.5)


def root(tree, id):
    while (tree[id] != id):
        tree[id] = tree[tree[id]]  # tree compression
        id = tree[id]
    return id


def union(tree, id1, id2):
    p = root(tree, id1)
    q = root(tree, id2)
    tree[p] = tree[q]


def kruskal(tree, distances, edges):
    for edge in edges:
        id1 = edge[0][2]
        id2 = edge[1][2]

        # check that a cycle isn't created
        if root(tree, id1) != root(tree, id2):
            union(tree, id1, id2)
            distances.append(edge[2])


N = int(input())

for i in range(N):
    S, P = [int(i) for i in input().split()]

    nodes = []
    edges = []  # contains the two nodes and the distance/weight between them
    distances = []  # distances of edges in the tree

    for j in range(P):  # read the nodes
        inp = input().split()
        nodes.append((int(inp[0]), int(inp[1]), j))  # nodes have x, y, and id

    # find all possible edges
    for j in range(len(nodes)):
        for k in range(j+1, len(nodes)):
            edges.append((nodes[j], nodes[k], distance(nodes[j], nodes[k])))

    # sort the edges using distances in ascending order
    edges.sort(key=lambda x: x[2])

    tree = [j for j in range(P)]  # use union find to represent the tree

    kruskal(tree, distances, edges)

    print('{:.2f}'.format(distances[-S]))
