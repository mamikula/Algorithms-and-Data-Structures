from queue import PriorityQueue
from math import inf

def Djikstra(graph, s):

    n = len(graph)
    parent = [-1]*n
    d = [inf]*n

    Q = PriorityQueue()
    d[s] = 0

    Q.put((d[s], s))

    while not Q.empty():
        u = Q.get()[1]

        for v in range(n):
            if graph[u][v] != -1:
                if d[v] > d[u] + graph[u][v]:
                    d[v] = d[u] + graph[u][v]
                    parent[v] = u
                    Q.put((d[v], v))


    return d


def KS(G, E, s, t):
    ds = Djikstra(G, s)
    dt = Djikstra(G, t)
    dtres = []
    dsres = []


    for e in E:
        e1 = e[0]
        e2 = e[1]
        ln = e[2]

        if abs(ds[e2] - ds[e1]) > ln:
            res = e
            dsres.append(e)


        if abs(dt[e2] - dt[e1]) > ln:
            dtres.append(e)

    print(res)
    print(dtres)
    print(dsres)

E = [(0, 3, 13), (1, 4, 2), (4, 5, 37), (0, 6, 1), (2, 5, -2)]
G = [
    [-1,3,5,-1,-1,-1,-1],
    [3,-1,-1,7,-1,-1,-1],
    [5,-1,-1,3,-1,-1,-1],
    [-1,7,3,-1,10,9,-1],
    [-1,-1,-1,10,-1,-1,4],
    [-1,-1,-1,9,-1,-1,2],
    [-1,-1,-1,-1,4,2,-1]
]

KS(G, E, 0, 6)