from math import inf

def Bellman_Ford(G, s):

    n = len(G)
    d = [inf]*n
    parent = [-1]*n

    d[s] = 0
    for k in range(n - 1):
        for u in range(n):
            for v in range(n):
                if G[u][v] != 0 and d[v] > d[u] + G[u][v] and v != s:
                    d[v] = d[u] + G[u][v]
                    parent[v] = u

    for u in range(n):
        for v in range(n):
            if G[u][v] != 0 and d[v] > d[u] + G[u][v]:
                return False

    return d

G =[[0,1,5,0,0],
    [1,0,2,7,8],
    [5,2,0,0,3],
    [0,7,0,0,1],
    [0,8,3,1,0]]

G2 = [[0, 1, 2, 3, 0],
    [0, 0, 0, 2, 4],
    [0, 0, 0, 0, 3],
    [0, 0, 1, 0, 1],
    [0, 0, 0, 0, 0]]

G3 = [[0, -1, 0],
      [0, 0, -1],
      [-1, 0, 0]]

print(Bellman_Ford(G2, 0))