def find(x, parent):
    if x != parent[x]:
        parent[x] = find(parent[x], parent)
    return parent[x]


def union(x, y, rank, parent):
    x = find(x, parent)
    y = find(y, parent)

    if x == y: return
    if rank[x] > rank[y]:
        parent[y] = x

    else:
        parent[x] = y
        if rank[x] == rank[y]:
            rank[y] += 1


def M2L(G):
    n = len(G)
    G1 = []
    for i in range(n):
        for j in range(n):
            if G[i][j] != 0:
                G1.append((i, j, G[i][j]))
                G[j][i] = 0
    G1.sort(key = lambda G:G[2])
    return G1


def Kruskal(G):
    A = []
    n = len(G)
    parent = [i for i in range(n)]
    rank = [0] * n
    G = M2L(G)
    for i in G:
        if find(i[0], parent) != find(i[1], parent):
            union(i[0], i[1], rank, parent)
            A.append(i)

    return A

W  = [
    [0,7,0,0,0,1],
    [7,0,2,0,3,8],
    [0,2,0,5,0,0],
    [0,0,5,0,6,4],
    [0,3,0,6,0,12],
    [1,8,0,4,12,0]]

G = [[0, 1, 2,],
     [1, 0, 3],
     [2, 3, 0]
     ]

print(Kruskal(G))